FROM ubuntu:20.04

RUN apt-get update -y && \
    apt install python3-pip python python-setuptools -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install virtualenv 
RUN pip3 install elastic-apm[flask] 
RUN pip3 install flask requests

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]