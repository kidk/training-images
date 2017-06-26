#!/usr/bin/env python
import MySQLdb
import time
import redis
import os

def calc_words(db, r):
    cur = db.cursor()
    print "Starting calc_words job"

    # Get words
    cur.execute("SELECT word FROM words ORDER BY number DESC LIMIT 10")

    # Set words in Redis
    counter = 1
    for row in cur.fetchall():
        print "Setting %s to %s" % (counter, row[0])
        r.set("string%s" % counter, row[0])
        counter = counter + 1

    cur.close()


if __name__ == '__main__':
    db = MySQLdb.connect(host=os.environ.get("DATABASE_HOST"), user=os.environ.get("DATABASE_USER"), passwd=os.environ.get("DATABASE_PASS"), db=os.environ.get("DATABASE_TABLE"))
    r = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

    if os.environ.get("LOOP") == "True":
        while True:
            calc_words(db, r)
            print "Sleeping 1 minute"
            time.sleep(60)
    else:
        calc_words(db, r)

    db.close()
