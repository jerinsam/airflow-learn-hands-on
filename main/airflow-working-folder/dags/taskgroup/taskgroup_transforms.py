from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# Task Group 
def taskgroup_transforms ():
    
    with TaskGroup('transforms_tg', tooltip = 'Tranform Tasks') as group:
        
        # Task 1
        transform_a_tg = BashOperator( 
            task_id='transform_a_tg',
            bash_command='sleep 10'
        )
    
        # Task 2
        transform_b_tg = BashOperator( 
            task_id='transform_b_tg',
            bash_command='sleep 10'
        )
    
        # Task 3
        transform_c_tg = BashOperator( 
            task_id='transform_c_tg',
            bash_command='sleep 10'
        )

        return group