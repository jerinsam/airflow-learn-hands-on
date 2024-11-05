from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime
  

my_dataset_file = Dataset('/tmp/dataset_for_triggering.csv')


# Initialize DAG
with DAG(
    dag_id="consumer",
    start_date=datetime(2023, 1, 1),
    schedule=[my_dataset_file],
    catchup=False
) as dag:
    
    @task
    def read_dataset():
        with open(my_dataset_file.uri,'r') as f:
            print(f.read())
    
    read_dataset()