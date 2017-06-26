FROM node:6-onbuild

MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

ENV RABBITMQ_HOST rabbitmq
ENV REDIS_HOST redis

LABEL com.coscale.monitoring='[{"PluginType":"APACHE","Configuration":{"FILE":["\"/var/log/nodejs.log\" \"%V \"%r\" %D %s\""],"URL CHECK":["http://localhost/ranking"]}}]'
