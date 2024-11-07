from airflow import DAG
from airflow.operators.bash import BashOperator 
from taskgroup.taskgroup_downloads import taskgroup_downloads # import taskgroup functions from taskgroup folder
from taskgroup.taskgroup_transforms import taskgroup_transforms # import taskgroup functions from taskgroup folder
 
from datetime import datetime
 
with DAG('parent_dag_for_taskgroup', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    
    # Task group  
    downloads_tg = taskgroup_downloads()
 
    check_files_tg = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
 
     # Task group  
    transforms_tg = taskgroup_transforms()
 
    downloads_tg >> check_files_tg >> transforms_tg