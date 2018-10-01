FROM alpine:3.7

LABEL maintainer Adam Strojek <adam@strojek.info>

EXPOSE 8080

RUN apk update
RUN apk add --upgrade --no-cache py-pip g++ python-dev linux-headers gcc make libffi-dev uwsgi-python uwsgi wget uwsgi-python3

RUN apk add --upgrade --no-cache python3 python3-dev postgresql-client postgresql-contrib postgresql-dev

ADD ./requirements.txt /tmp

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

ADD . /code/
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
