#!/bin/bash

#
# This script will deploy the latest version of our application in Swarm
#

curl https://raw.githubusercontent.com/kidk/training-images/master/docker-swarm/docker-compose.yml > /tmp/docker-compose.yml
docker stack deploy --compose-file /tmp/docker-compose.yml words
rm /tmp/docker-compose.yml
