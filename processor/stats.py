#!/usr/bin/python
import sys
import json
import random
import time
import MySQLdb

db = MySQLdb.connect(host="database", user="root", passwd="secret", db="my_db")        
cur = db.cursor()

# Configuration mode: return the custom metrics data should be defined
def config():
    settings = {
        "maxruntime": 5000,  # How long the script is allowed to run
        "period": 60,  # The period the script will run, in this case it will run every 60 seconds
        "metrics": [
            {
                "id": 0,
                "datatype": "DOUBLE",
                "name": "Number of words",
                "description": "Total number of words in database",
                "groups": "Statistics",
                "unit": "#",
                "tags": "",
                "calctype": "Instant"
            },
            {
                "id": 1,
                "datatype": "DOUBLE",
                "name": "Average length",
                "description": "Average word length",
                "groups": "Statistics",
                "unit": "#",
                "tags": "",
                "calctype": "Instant"
            },
            {
                "id": 2,
                "datatype": "DOUBLE",
                "name": "Average word use",
                "description": "Average number of times word is used",
                "groups": "Statistics",
                "unit": "#",
                "tags": "",
                "calctype": "Instant"
            }
        ]
    }

    print json.dumps(settings)

# Data retrieval mode: return the data for the custom metrics
def data():
    # Find row
    cur.execute("SELECT COUNT(*), AVG(LENGTH(word)), AVG(number) FROM words")
    row = cur.fetchone()

    print "M0 %s" % row[0]
    print "M1 %s" % row[1]
    print "M2 %s" % row[2]


# Switch to check in which mode the script is running
if __name__ == "__main__":
    if sys.argv[1] == '-c':
        config()
    if sys.argv[1] == '-d':
        data()
