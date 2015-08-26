FROM python:3.4
MAINTAINER lee ho sung

RUN pip install redis

RUN mkdir /code
ADD . /code
WORKDIR /code

CMD python -m unittest discover
