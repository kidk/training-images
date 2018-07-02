#!/usr/bin/env python
import pika
import MySQLdb
import time
import os

CLEANUP_THRESHOLD = os.environ.get("CLEANUP_THRESHOLD")
db = MySQLdb.connect(host=os.environ.get("DATABASE_HOST"), user=os.environ.get("DATABASE_USER"), passwd=os.environ.get("DATABASE_PASS"), db=os.environ.get("DATABASE_TABLE"))

# Create database for results
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS words (`id` int NOT NULL AUTO_INCREMENT, `word` VARCHAR(255) NOT NULL, `number` INT, PRIMARY KEY (id), UNIQUE(word));")

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ.get("RABBITMQ_HOST")))
channel = connection.channel()

# Select queue
channel.queue_declare(queue='messages')

# Message received callback
def callback(ch, method, properties, body):
    body = body.lower()
    print("Received %s" % body)
    start = time.time()

    for word in body.split():
        # Find row
        cur.execute("SELECT * FROM words WHERE word = '%s'" % word)

        # If not exists create
        if cur.rowcount == 0:
            cur.execute("INSERT INTO words (word, number) VALUES ('%s', 0)" % word)

        # Increment row
        cur.execute("UPDATE words SET number = number + 1 WHERE word = '%s'" % word)

        db.commit()

    time_taken = time.time() - start
    print("Finished processing %s in %s ms" % (body, time_taken))

    print("Starting cleanup")
    cur.execute("SELECT COUNT(id) FROM words")
    amount = cur.fetchone()[0]
    if amount > CLEANUP_THRESHOLD:
        cur.execute("DELETE FROM words LIMIT %s" % (amount - CLEANUP_THRESHOLD))
    print("Finished cleanup")

# Wait for message
channel.basic_consume(callback,
                      queue='messages',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
