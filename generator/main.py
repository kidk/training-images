import time
import requests
import random
import os

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
    print "get request"
    requests.get("http://%s" % WEB_HOST)

def request_post():
    sentence = random_sentence()
    print "post request with word: %s" % sentence
    requests.post("http://%s/post" % RECEIVER_HOST, data={'text': sentence})


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
