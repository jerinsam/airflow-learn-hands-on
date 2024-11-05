from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime
  

my_dataset_file = Dataset('/tmp/dataset_for_triggering.csv')


# Initialize DAG
with DAG(
    dag_id="producer",
    start_date=datetime(2023, 1, 1),
    schedule ="@daily",
    catchup=False
) as dag:
    
    @task(outlets = [my_dataset_file])
    def update_dataset():
        with open(my_dataset_file.uri,'a+') as f:
            f.write('producer_udpate')
    
    update_dataset()