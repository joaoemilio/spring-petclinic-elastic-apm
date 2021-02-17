FROM ubuntu:20.04

RUN apt-get update -y && \
    apt install git python3-pip python python-setuptools -y

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /usr/src/
COPY build.txt .
RUN cat build.txt && git clone https://github.com/joaoemilio/spring-petclinic-elastic-apm.git
WORKDIR /usr/src/spring-petclinic-elastic-apm/address_resolver/src
RUN pip3 install gunicorn json-logging-py 
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
#WORKDIR /opt/bot_server

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "gunicorn.conf", "--log-config", "logging.conf", "-b", ":5000", "server:app"]