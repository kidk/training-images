FROM richarvey/nginx-php-fpm

MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

ENV RECEIVER_HOST receiver

COPY src/ /var/www/html/

# CoScale configuration
COPY nginx.conf /etc/nginx/
# End of CoScale configuration
