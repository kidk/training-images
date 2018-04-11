#!/bin/bash

#
# This script will deploy the latest version of our application in Kubernetes
#

NAMESPACE=${1:-coscale-micro}

oadm new-project $NAMESPACE
oc project $NAMESPACE
oadm policy add-scc-to-user anyuid -z default
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/mysql.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/rabbitmq.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/redis.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/receiver.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/web.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/services.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_letters.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_words.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/generator.yaml
oc apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/processor.yaml
