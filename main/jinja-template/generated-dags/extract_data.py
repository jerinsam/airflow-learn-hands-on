from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

with DAG(dag_id="extract_data",start_date=datetime(2022,1,1) ,schedule="@daily",catchup=False) as dag:
    create_table= PostgresOperator(
        task_id="create_table",
        #<Insert Code>#
    )

    get_data= PostgresOperator(
        task_id="get_data",
        #<Insert Code>#
    )

    # Dependency 
    create_table >> get_data