#!/usr/bin/env python
import pika
import MySQLdb
import time

db = MySQLdb.connect(host="database", user="root", passwd="secret", db="my_db")        

# Create database for results
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS words (`id` int NOT NULL AUTO_INCREMENT, `word` VARCHAR(255) NOT NULL, `number` INT, PRIMARY KEY (id), UNIQUE(word));")

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq'))
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


# Wait for message
channel.basic_consume(callback,
                      queue='messages',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
