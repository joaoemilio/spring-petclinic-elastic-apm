FROM openjdk:8

WORKDIR /app

COPY *.jar ./
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]