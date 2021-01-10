FROM node:10.19

WORKDIR /usr/src/
RUN git clone https://github.com/joaoemilio/spring-petclinic-elastic-apm.git
ENV PATH /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client/node_modules/.bin:$PATH

WORKDIR /usr/src/spring-petclinic-elastic-apm/frontend_client_server/client
RUN npm install
RUN npm install --unsafe-perm
RUN npm run build:prod

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
