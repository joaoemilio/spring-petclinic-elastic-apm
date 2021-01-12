java -javaagent:elastic-apm-agent.jar \
 -Delastic.apm.service_name=petclinic-java \
 -Delastic.apm.server_urls=$ELASTIC_APM_SERVER_URL \
 -Delastic.apm.secret_token=$ELASTIC_APM_SECRET_TOKEN \
 -Delastic.apm.application_packages=org.springframework.samples.petclinic \
 -jar spring-petclinic.jar 