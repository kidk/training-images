#!/usr/bin/env python
import MySQLdb
import time
import redis
import os

db = MySQLdb.connect(host=os.environ.get("DATABASE_HOST"), user=os.environ.get("DATABASE_USER"), passwd=os.environ.get("DATABASE_PASS"), db=os.environ.get("DATABASE_TABLE"))        
cur = db.cursor()

r = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

print "Starting calc_words job"

# Get words
cur.execute("SELECT word FROM words ORDER BY number DESC LIMIT 10")

# Set words in Redis
counter = 1
for row in cur.fetchall():
    print "Setting %s to %s" % (counter, row[0])
    r.set("string%s" % counter, row[0])
    counter = counter + 1

db.close()
