FROM python:3.8

RUN /bin/sh -c "apt-get update && apt-get install -y postgresql-client"
RUN /bin/sh -c "apt-get install -y gunicorn python3-psutil"

WORKDIR /web
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

