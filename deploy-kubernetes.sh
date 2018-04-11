#!/bin/bash

#
# This script will deploy the latest version of our application in Kubernetes
#

NAMESPACE=${1:-coscale-micro}

kubectl create namespace $NAMESPACE
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/mysql.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/rabbitmq.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/redis.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/receiver.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/web.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/services.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_letters.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_words.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/generator.yaml
kubectl apply -n $NAMESPACE -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/processor.yaml
