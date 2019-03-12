FROM python:3.6.8-stretch

MAINTAINER shuai.zhang <shuai.zhang.2000@gmail.com>

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -q -r requirements.txt

ENV PYTHONPATH $PYTHONPATH:/app

ADD python/backend/ /app/backend/

CMD ["uwsgi", "--ini", "/app/backend/uwsgi.ini"]

