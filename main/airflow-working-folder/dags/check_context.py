from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
 
from datetime import datetime
 

def _t1(**context): # call DAG context 
    print("-"*100)
    print(type(context)) # shows context is of type dict
    print("-"*100)
    print(context)
    print("-"*100)
    print(context["dag"])
    print("-"*100)
    print(context["dag"].dag_id)
  
 
with DAG("check_context", start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
   