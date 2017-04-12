#!/usr/bin/env python
import MySQLdb
import time
import redis

db = MySQLdb.connect(host="database", user="root", passwd="secret", db="my_db")        
cur = db.cursor()

r = redis.StrictRedis(host='redis')

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
