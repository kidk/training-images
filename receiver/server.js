var express = require('express');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var fs = require('fs');
var path = require('path');

var redis = require("redis"),
  client = redis.createClient({
    "host": "redis"
  });

var amqp = require('amqplib/callback_api');
var channel;
var q = 'messages';
amqp.connect('amqp://rabbitmq', function (err, conn) {
  conn.createChannel(function (err, ch) {

    ch.assertQueue(q, {
      durable: false
    });
    channel = ch;
  });
});

var app = express();
// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(path.join('/var/log/nodejs.log'), {flags: 'a'})
app.use(morgan("receiver \":method :url HTTP/:http-version\" :response-time :status", {stream: accessLogStream}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: false
}));

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

app.listen(80, function () {
  console.log('App is listening on port 80');
});
