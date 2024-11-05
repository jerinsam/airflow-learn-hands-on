
###### Go to the folder path where docker-compose.yaml file is kept and execute below script to list all active containers.
    docker-compose ps

###### Open the Airflow docker shell from the Host Machine, using the below script.
    # code snippet: docker exec -it <container_name>  /bin/bash
    docker exec -it 2-airflow-docker-configure-airflow-scheduler-1 /bin/bash

###### Test the shell by using below script, this will help to check whether airflow is accessible or not.
    airflow -h

###### Test Airflow tasks using below script: 
    # code snippet: airflow tasks test <dag_id> <task_id> <past-date>
    airflow tasks test user_processing create_table 2022-01-01

