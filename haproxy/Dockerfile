FROM haproxy

MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

RUN touch /var/log/haproxy.log

COPY haproxy.cnf /usr/local/etc/haproxy/haproxy.cfg

LABEL com.coscale.monitoring='[{"PluginType":"RABBITMQ","Configuration":{"HOSTNAME":["localhost"],"PORT":["15672"],"USERNAME":["guest"],"PASSWORD":["guest"],"AMQP PORT":["5672"],"QUEUE":["coscale"]}},{"PluginType":"HAPROXY","Configuration":{"FILE":["\"/var/log/haproxy.log\" \"%hr\\ %{+Q}r\\ %Tt\\ %ST\\ %B\""],"STATS URL":["http://someuser:somepass@localhost:1936/haproxy?stats"],"URL CHECK":["http://localhost"]}}]'