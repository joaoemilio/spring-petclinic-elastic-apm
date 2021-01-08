java -javaagent:elastic-apm-agent-1.19.0.jar \
 -Delastic.apm.service_name=petclinic-java \
 -Delastic.apm.server_urls=https://e502ba7b9aac4941a32d366eb20628c0.apm.southamerica-east1.gcp.elastic-cloud.com \
 -Delastic.apm.secret_token=fUdDairnKQ5L6CUq8U \
 -Delastic.apm.application_packages=org.springframework.samples.petclinic \
 -jar target/spring-petclinic-1.5.16.jar 