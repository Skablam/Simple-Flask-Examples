FROM ubuntu:12.04
MAINTAINER Skablam
RUN apt-get -qq update
RUN apt-get -qqy install python python-pip
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN mkdir /code
WORKDIR /code
ADD . /code
CMD python /code/run.py
