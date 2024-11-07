from airflow import DAG
from airflow.operators.bash import BashOperator

# Subdag 
def subdag_transforms (parent_id, child_id, args):
    
    with DAG(
        f'{parent_id}.{child_id}', start_date = args['start_date'],
        schedule_interval = args['schedule_interval'],
        catchup = args['catchup']
        ) as dag:

        # Task 1
        transform_a = BashOperator( 
            task_id='transform_a',
            bash_command='sleep 10'
        )
    
        # Task 2
        transform_b = BashOperator( 
            task_id='transform_b',
            bash_command='sleep 10'
        )
    
        # Task 3
        transform_c = BashOperator( 
            task_id='transform_c',
            bash_command='sleep 10'
        )

        return dag