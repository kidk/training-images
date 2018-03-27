import time
import requests
import random
import os
import sys

WEB_HOST = os.environ.get("WEB_HOST")
RECEIVER_HOST = os.environ.get("RECEIVER_HOST")

# Read possible words
with open('words.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# Split
words = data.split(" ")
print "Found %s possible words" % len(words)

def random_word():
    result = ""
    for number in range(1, random.randint(2, 5)):
        result = result + random.choice (words)

    return result

def random_sentence():
    result = ""
    for number in range(5, random.randint(10, 20)):
        result = result + " " + random_word()

    return result

def request_get():
    try:
        print "get request"
        requests.get("http://%s:8080" % WEB_HOST)
        requests.get("http://%s:8080/stats" % WEB_HOST)
        requests.get("http://%s:8080/stats/ranking" % WEB_HOST)
        requests.get("http://%s:8080/stats/letters" % WEB_HOST)
        requests.get("http://%s:8080/submit" % WEB_HOST)
    except: # catch *all* exceptions
        print "Exception: %s" % sys.exc_info()[0]

def request_post():
    try:
        sentence = random_sentence()
        print "post request with word: %s" % sentence
        requests.post("http://%s:8080/post" % RECEIVER_HOST, data={'text': sentence})
    except: # catch *all* exceptions
        print "Exception: %s" % sys.exc_info()[0]


while True:
    # Do a certain number of requests depending on the time of day
    start = time.time()

    timeInDay = start % 86400
    if timeInDay > (86400 / 2):
        timeInDay = 86400 - timeInDay

    numberOfRequests = int(round(timeInDay / 1350)) + 1
    for number in range(0, numberOfRequests):
        request_get()

    # Submit data to the services
    request_post()
    time_taken = int((time.time() - start) * 1000)

    # Write to logfile
    with open("/var/log/generator.log", "a") as myfile:
        myfile.write("%s\n" % time_taken)

    time.sleep(5)
