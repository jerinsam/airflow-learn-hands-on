from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads  # import subdag functions from subdag folder
from subdags.subdag_transforms import subdag_transforms  # import subdag functions from subdag folder
 
from datetime import datetime
 
with DAG('parent_dag_for_subdags', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    args = {'start_date':dag.start_date,'schedule_interval': dag.schedule_interval, 'catchup':dag.catchup }
    
    # SubDag Task
    downloads = SubDagOperator(
        task_id = 'downloads',
        subdag = subdag_downloads( parent_id = dag.dag_id, child_id = 'downloads',args = args)
    )
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
 
    transforms = SubDagOperator(
        task_id = 'transforms',
        subdag = subdag_transforms( parent_id = dag.dag_id, child_id = 'transforms',args = args)
    )
 
    downloads >> check_files >> transforms