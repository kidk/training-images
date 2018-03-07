#!/bin/bash

#
# This script will deploy the latest version of our application in Kubernetes
#

oadm new-project coscale-micro
oc project coscale-micro
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/mysql.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/rabbitmq.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/redis.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/receiver.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/web.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/services.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_letters.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_words.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/generator.yaml
oc apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/processor.yaml
