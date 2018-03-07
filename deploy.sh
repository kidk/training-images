#!/bin/bash

#
# This script will deploy the latest version of our application
#

NAMESPACE=${1:-training}

kubectl create namespace $NAMESPACE
kubectl apply -f kubernetes/mysql.yaml -n $NAMESPACE
kubectl apply -f kubernetes/rabbitmq.yaml -n $NAMESPACE
kubectl apply -f kubernetes/redis.yaml -n $NAMESPACE
kubectl apply -f kubernetes/receiver.yaml -n $NAMESPACE
kubectl apply -f kubernetes/web.yaml -n $NAMESPACE
kubectl apply -f kubernetes/services.yaml -n $NAMESPACE
kubectl apply -f kubernetes/calc_letters.yaml -n $NAMESPACE
kubectl apply -f kubernetes/calc_words.yaml -n $NAMESPACE
kubectl apply -f kubernetes/generator.yaml -n $NAMESPACE
kubectl apply -f kubernetes/processor.yaml -n $NAMESPACE
