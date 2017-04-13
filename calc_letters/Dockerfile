FROM python:2-onbuild

MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>

ENV DATABASE_HOST database
ENV DATABASE_USER root
ENV DATABASE_PASS secret
ENV DATABASE_TABLE my_db
ENV REDIS_HOST redis

CMD [ "python", "./main.py" ]

