

###### In this tutorial, Airflow Docker container will be used #######
# Docker Compose url : https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml 
# Download docker-compose.yaml file from the above URL

# Download Docker Desktop for Windows and run it
# Execute the below command to pull and configure all the images defined in the docker-compose.yaml file
# this needs to be executed in the same folder where docker-compose.yaml file exists

docker compose up -d # to start all the services mentioned in the docker compose yaml file
 

docker-compose stop # to stop all container services  