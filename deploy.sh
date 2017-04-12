#!/bin/bash

#
# This script will deploy the latest version of our application
#

function stop {
    NAME=$1
    RUNNING=$(docker inspect --format="{{ .State.Running }}" $NAME)
    
    if [ "$RUNNING" == "true" ]; then
        echo "Stopping container $NAME"
        docker stop $NAME > /dev/null   
    fi

    # Clean up container environment
    docker rm $(docker ps -a -q) 2> /dev/null > /dev/null
}

# Create network for containers 
docker network create coscale

# Stop all containers
stop generator
stop processor
stop redis
stop rabbitmq
stop database
stop nginx01
stop nginx02
stop nginx03
stop receiver
stop haproxy
sleep 5

# Redis
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name redis local/redis

# RabbitMQ
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name rabbitmq local/rabbitmq

# MySQL
stop database
docker run -t -d --net=coscale -v /root/mysqldata:/var/lib/mysql --restart unless-stopped --name database local/mysql
sleep 5

# Nginx containers
echo "Starting nginx containers"
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name nginx01 local/nginx
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name nginx02 local/nginx
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name nginx03 local/nginx
echo

# Receiver
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name receiver local/receiver

# Processor
docker run -t -d \
    --net=coscale \
    --restart unless-stopped \
    --name processor local/processor

# Haproxy
docker run -t -d \
    -p 80:80 \
    --restart unless-stopped \
    --net=coscale \
    --name haproxy local/haproxy

# Generator
docker run -t -d \
    --restart unless-stopped \
    --net=coscale \
    --name generator local/generator
