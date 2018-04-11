#!/bin/bash

#
# This script will deploy the latest version of our application in Swarm
#

NAMESPACE=${1:-coscale-micro}

curl https://raw.githubusercontent.com/kidk/training-images/master/docker-swarm/docker-compose.yml > /tmp/docker-compose.yml
docker stack deploy --compose-file /tmp/docker-compose.yml $NAMESPACE
rm /tmp/docker-compose.yml
