from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.variable import Variable
from airflow.decorators import task
 
from datetime import datetime
   
with DAG("check_variables_task_decorator", start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
    
    # Task to set the values of Variables using set method of Variable class
    @task
    def set_variables():
        Variable.set(key = "variableName",value = "Jerin")
        Variable.set(key = "variableAdditionalAttributes", value = {"Age":33,"Company":"Aligned Automation"}, serialize_json= True)
    
    set_variables_task = set_variables()

    # Task to get the values of Variables using get method of Variable class
    @task
    def get_variables():
        Name = Variable.get(key = "variableName", default_var = None)
        Age = Variable.get(key = "variableAdditionalAttributes", deserialize_json= True, default_var = None)['Age']
        Company = Variable.get(key = "variableAdditionalAttributes", deserialize_json= True, default_var = None)['Company']

        print(f"Hi! My name is {Name}, I'm {Age} years old and I'm working with {Company}")
    
    get_variables_task =  get_variables()

    # Task to get the values of Variables using context
    @task
    def get_variables_context(**context):
        Name = context['var']['value'].get("variableName")
        Age = context['var']['json'].get("variableAdditionalAttributes")["Age"]
        Company = context['var']['json'].get("variableAdditionalAttributes")["Company"]

        print(f"Hi Context! My name is {Name}, I'm {Age} years old and I'm working with {Company}")

    get_variables_context_task = get_variables_context()

    # Set Dependency
    set_variables_task >> get_variables_task >> get_variables_context_task