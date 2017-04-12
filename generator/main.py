import time
import requests
import random

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
    requests.get("http://haproxy")

def request_post():
    sentence = random_sentence()
    print "post request with word: %s" % sentence
    requests.post("http://receiver/post", data={'text': sentence})


while True:
    # Do 10 request
    start = time.time()
    for number in range(0, 9):
        request_get()

    request_post()
    time_taken = int((time.time() - start) * 1000)

    # Write to logfile
    with open("/var/log/generator.log", "a") as myfile:
        myfile.write("%s\n" % time_taken)

    time.sleep(5)
