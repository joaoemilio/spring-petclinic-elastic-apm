_image_name=petclinic-java-elastic-apm
_image_version=v1.0.$1
_repository=joaoemilio

echo $PWD

echo "compiling and packaging spring boot jar file"
mvn compile package -DskipTests

cp target/spring*.jar ./spring-petclinic.jar

echo "build image"
docker build . -t $_image_name:$_image_version
echo "tagging image"
docker tag $_image_name:$_image_version $_repository/$_image_name:$_image_version 
docker tag $_image_name:$_image_version $_repository/$_image_name:latest
echo "pushing image"
docker push $_repository/$_image_name:$_image_version