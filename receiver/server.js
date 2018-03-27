var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');
var path = require('path');

// Initiate app
var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: false
}));

// Initiate prometheus client and metrics
const promClient = require('prom-client');
const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics({ timeout: 1000 })
const promLatency = new promClient.Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'code'],
  // buckets for response time from 0.1ms to 500ms
  buckets: [0.10, 5, 15, 50, 100, 200, 300, 400, 500]
})
const promRate = new promClient.Counter({
  name: 'http_request_count',
  help: 'Number of HTTP requests',
  labelNames: ['method', 'route', 'code']
})

// Register start time for each request
app.use((req, res, next) => {
  res.locals.startEpoch = Date.now()
  next()
})

var redis = require("redis"),
  client = redis.createClient({
    "host": process.env.REDIS_HOST
  });

var amqp = require('amqplib/callback_api');
var channel;
var q = 'messages';
amqp.connect('amqp://' + process.env.RABBITMQ_HOST, function (err, conn) {
  console.log(err);
  conn.createChannel(function (err, ch) {
    ch.assertQueue(q, {
      durable: false
    });
    channel = ch;
  });
});

app.get('/ranking', function (req, res) {
  var result = [];
  var elements = [];

  for (var i = 1; i < 11; i++) {
    elements.push("string" + i);
  }

  client.mget(elements, function (err, reply) {

    for (var i = 0; i < 10; i++) {
      result.push({
        "position": i + 1,
        "value": reply[i]
      });
    }

    res.send(JSON.stringify(result));

  });
});


app.get('/letters', function (req, res) {
  var result = []
  var alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  var elements = []

  for (var i = 0; i < alphabet.length; i++) {
    elements.push("alfa" + alphabet[i]);
  }

  client.mget(elements, function (err, reply) {

    for (var i = 0; i < alphabet.length; i++) {
      result.push({
        "letter": alphabet[i],
        "value": reply[i]
      });
    }

    res.send(JSON.stringify(result));

  });
});

app.post('/post', function (req, res) {
  var result = channel.sendToQueue(q, new Buffer(req.body.text));
  res.send(JSON.stringify(result));
});

// Provide prometheus endpoint to collect data
app.get('/metrics', (req, res) => {
  // Deny connections from outside container
  var remote = req.ip || req.connection.remoteAddress
  if ((remote !== '::1') && (remote !== 'localhost') && (remote !== '::ffff:127.0.0.1')) {
    return res.status(401).send();
  }

  // Return prometheus metrics
  res.set('Content-Type', promClient.register.contentType)
  res.end(promClient.register.metrics())
})

// Register stop time for each request and pass to prometheus
app.use((req, res, next) => {
  const responseTimeInMs = Date.now() - res.locals.startEpoch

  promLatency
    .labels(req.method, req.route.path, res.statusCode)
    .observe(responseTimeInMs)
  promRate
    .labels(req.method, req.route.path, res.statusCode)
    .inc()

  next()
})

app.listen(8080, function () {
  console.log('App is listening on port 8080');
});
