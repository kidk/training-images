#!/bin/bash

#
# This script will build a certain docker image from the images directory
#

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <service>"
  exit 1
fi

function build {
  NAME=$1

  echo "Building $NAME"
  pushd $NAME
  docker build --no-cache -t local/$NAME:latest .
  popd
  echo
}

COMMAND=$1

if [ "$COMMAND" == "all" ]; then
  build haproxy
  build nginx
  build receiver
  build redis
  build rabbitmq
  build mysql
  build processor
  build calc_words
  build calc_letters
  build generator
else
  build $COMMAND
fi
