# Composer
FROM composer:1.6 as composer
COPY . /src
WORKDIR /src/app
RUN composer install --no-dev

# Build
FROM php:7.1-apache
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

ENV RECEIVER_HOST receiver

RUN a2enmod rewrite
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY apache2.conf /etc/apache2/apache2.conf
COPY status-page.conf /etc/apache2/conf-enabled/status-page.conf

COPY app/ /var/www/app/
COPY --from=composer /src/app/vendor /var/www/vendor

LABEL com.coscale.monitoring='[{"PluginType":"APACHE","Configuration":{"FILE":["\"/dev/stdout\" \"%V \"%r\" %D %s %I %O\""],"STATS URL":["http://localhost/server-status"],"URL CHECK":["http://localhost/"]}}]'
