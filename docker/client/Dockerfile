FROM node:10.19

WORKDIR /usr/src/
COPY build.txt .
RUN cat build.txt && git clone https://github.com/joaoemilio/spring-petclinic-elastic-apm.git /usr/src/spring-petclinic-elastic-apm
ENV PATH /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/node_modules/.bin:$PATH

WORKDIR /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/
RUN npm install && npm install --unsafe-perm && npm run build:prod

ENV NODE_ENV=production
WORKDIR /usr/src/spring-petclinic-elastic-apm/frontend_client_server/server

ENV PATH /usr/src/spring-petclinic-elastic-apm/frontend_client_server/server/node_modules/.bin:$PATH
RUN npm install
RUN cp /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/dist/index.* /usr/src/spring-petclinic-elastic-apm/frontend_client_server/server/public/
RUN cp -R /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/dist/public/ /usr/src/spring-petclinic-elastic-apm/frontend_client_server/server/public/

COPY sourcemaps /source_maps
RUN cp /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/dist/index.js.map /source_maps/index.js.map

COPY entrypoint.sh /etc/entrypoint.sh

ENV NODE_ENV production
EXPOSE 3000
CMD ["npm","start"]
ENTRYPOINT ["/bin/bash", "/etc/entrypoint.sh"]
