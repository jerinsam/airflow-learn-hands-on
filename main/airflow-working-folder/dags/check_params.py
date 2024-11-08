from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.param import Param
 
from datetime import datetime
 

def _t1(**context): # call DAG context 
    print("-"*100)
    print(context["params"]["Name"]) # Access Paramter Name
    print("-"*100)
    print(context["params"]["Age"])# Access Paramter Age
 
with DAG("check_params", start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False,
    params={
        "Name": "Dummy","Age": Param(999,type="integer")}
        ) as dag:
 
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
   