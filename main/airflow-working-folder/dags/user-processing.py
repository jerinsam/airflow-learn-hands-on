from airflow import DAG
from datetime import datetime

from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator

import JSON

# Process Data
def _process_user(ti):
    user = ti.xcom_pull(task_id = 'extract_user')
    user = user['results'][0]
    processed_user=json_normalize({
        'firstname':user['name']['first'],
        'lastname':user['name']['last'],
        'country':user['lcoation']['country'],
        'username':user['login']['username'],
        'password':user['login']['password'],
        'email':user['email'],
    })
    processed_user.to_csv('/tmp/processed_user.csv',index=None,header=False)


# Initialize DAG
with DAG(
    dag_id="user_processing",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    # Task 1- create table in postgres
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        ''')
        
    # Task 2- check API is available or not using sensor task
    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id = 'user_api',
        endpoint = 'api/'
        )
     

    # Task 3- extract user data from API
    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',
        endpoint='api/',
        method = 'GET',
        response_filter = lambda response: json.loads(response.text),
        log_response = True
        )

    # Task 4- Process Data using Python Operator
    process_user = PythonOperator(
        task_id='process_user',
        python_callable = _process_user
        )
    
    # Define Dependency
    extract_user >> process_user