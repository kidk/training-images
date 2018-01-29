FROM node:6-onbuild

MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

ENV RABBITMQ_HOST rabbitmq
ENV REDIS_HOST redis

LABEL com.coscale.monitoring='[{"PluginType":"PROMETHEUS","Configuration":{"STATS URL":["http://127.0.0.1/metrics"]}},{"PluginType":"ENDPOINTCHECKER","Configuration":{"ENDPOINT":["http://127.0.0.1/ranking"]}}]'
