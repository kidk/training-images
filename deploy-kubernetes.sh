#!/bin/bash

#
# This script will deploy the latest version of our application in Kubernetes
#

kubectl create namespace coscale-micro
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/mysql.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/rabbitmq.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/redis.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/receiver.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/web.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/services.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_letters.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/calc_words.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/generator.yaml
kubectl apply -f https://raw.githubusercontent.com/kidk/training-images/master/kubernetes/processor.yaml
