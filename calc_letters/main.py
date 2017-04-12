#!/usr/bin/env python
import MySQLdb
import time
import redis
import string

db = MySQLdb.connect(host="database", user="root", passwd="secret", db="my_db")        
cur = db.cursor()

r = redis.StrictRedis(host='redis')

print "Starting calc_words job"

# Get words
cur.execute("SELECT word, number FROM words")

def position(letter):
    return ord(letter) - 97

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

db.close()
