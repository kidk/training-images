# Training images

Set of images used in CoScale demo and training environment. **Do not deploy these in a production environment!**

## Deployment

### Kubernetes

```
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
```

### Docker Swarm

```
curl https://raw.githubusercontent.com/kidk/training-images/master/docker-swarm/docker-compose.yml > docker-compose.yml
docker stack deploy --compose-file docker-compose.yml words
```
