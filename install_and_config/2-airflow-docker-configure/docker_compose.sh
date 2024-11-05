

###### In this tutorial, Airflow Docker container will be used #######
# Docker Compose url : https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml 

""" Follow following Steps to setup Docker container for Airflow
# 1. Download docker-compose.yaml file from the above URL
# 2. If Windows OS is being used then replace volume Environmental varialble (${AIRFLOW_PROJ_DIR:-.}) to windows folder. (for ref. check the docker compose file present here).
# 3. Download Docker Desktop for Windows and run it
# 4. Execute the below command to pull and configure all the images defined in the docker-compose.yaml file
# these commands need to be executed in the same folder where docker-compose.yaml file exists

Step 2 is required to mount host system folder to Airflow Docker, this will help to move files between Host and Docker 
"""

docker compose up -d # to start all the services mentioned in the docker compose yaml file
 

docker-compose stop # to stop all container services  