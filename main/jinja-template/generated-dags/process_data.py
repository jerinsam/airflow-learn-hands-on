from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

with DAG(dag_id="process_data",start_date=datetime(2022,1,1) ,schedule="@daily",catchup=False) as dag:
    process_data= PythonOperator(
        task_id="process_data",
        #<Insert Code>#
    )

    get_api_data= BashOperator(
        task_id="get_api_data",
        #<Insert Code>#
    )

    # Dependency 
    process_data >> get_api_data