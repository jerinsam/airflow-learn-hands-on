from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# Task Group 
def taskgroup_downloads():
    with TaskGroup('downloads_tg',tooltip = 'Download Tasks') as group:

        # Task 1
        download_a_tg = BashOperator(
            task_id='download_a_tg',
            bash_command='sleep 10'
        )
    
        # Task 2
        download_b_tg = BashOperator(
            task_id='download_b_tg',
            bash_command='sleep 10'
        )
    
        # Task 3
        download_c_tg = BashOperator(
            task_id='download_c_tg',
            bash_command='sleep 10'
        )

        return group