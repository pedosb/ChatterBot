FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update &&\
    apt-get -y upgrade &&\
    apt-get -y install --no-install-recommends \
        python-pip git python-setuptools python-levenshtein &&\
    git clone https://github.com/pedosb/ChatterBot &&\
    apt-get remove --purge -y git &&\
    apt-get autoremove -y &&\
    rm -rf /var/lib/apt/lists /tmp/*

RUN cd /ChatterBot &&\
    pip install -r requirements.txt &&\
    pip install django

WORKDIR /ChatterBot/examples/django_app

RUN PYTHONPATH=/ChatterBot/ python manage.py migrate

RUN mkdir -p /bootstrap && \
    mv /ChatterBot /bootstrap/ChatterBot

WORKDIR /

ENTRYPOINT \
    if [ ! -d /data/ChatterBot ]; \
    then \
        mkdir -p /data &&\
        cp -a /bootstrap/ChatterBot /data/ChatterBot; \
    fi; \
    cd /data/ChatterBot/examples/django_app &&\
    PYTHONPATH=/data/ChatterBot/ python manage.py runserver 0.0.0.0:8000
