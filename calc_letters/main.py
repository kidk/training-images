#!/usr/bin/env python
import MySQLdb
import time
import redis
import string
import os

def position(letter):
    return ord(letter) - 97


def calc_letters(db, r):
    print "Starting calc_letters job"
    cur = db.cursor()

    # Get words
    cur.execute("SELECT word, number FROM words")

    # Data array
    letters = list(string.ascii_lowercase)
    data = []
    for letter in letters:
        data.insert(position(letter), 0)

    print "Starting word processing"
    # Calculate letter usage
    for row in cur.fetchall():
        word = row[0].lower()
        count = row[1]

        print "Processing word %s" % word
        for letter in list(word):
            if letter in letters:
                data[position(letter)] = data[position(letter)] + count

    print "Finished with word processing"
    print
    print "Saving data"
    # Setting data in redis
    for letter in letters:
        print "Setting letter %s to %s" % (letter, data[position(letter)])
        r.set("alfa%s" % letter, data[position(letter)])

    cur.close()


if __name__ == '__main__':
    db = MySQLdb.connect(host=os.environ.get("DATABASE_HOST"), user=os.environ.get("DATABASE_USER"), passwd=os.environ.get("DATABASE_PASS"), db=os.environ.get("DATABASE_TABLE"))
    r = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

    if os.environ.get("LOOP") == "True":
        while True:
            calc_letters(db, r)
            print "Sleeping 1 minute"
            time.sleep(60)
    else:
        calc_letters(db, r)

    db.close()
