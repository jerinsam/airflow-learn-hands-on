from airflow import DAG
from airflow.operators.bash import BashOperator

# Subdag 
def subdag_downloads(parent_id, child_id, args : dict):
    
    with DAG(
        f'{parent_id}.{child_id}', start_date = args['start_date'],
        schedule_interval = args['schedule_interval'],
        catchup = args['catchup']
        ) as dag:

        # Task 1
        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )
    
        # Task 2
        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )
    
        # Task 3
        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )

        return dag