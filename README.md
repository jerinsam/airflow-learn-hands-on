## LEARN KAFKA
**DATA ENGINEERING - Learn Airflow**
This repo covers Airflow tutorial and for this tutorial Airflow Docker distribution is used.

**Following Services are covered -**
1. Airflow
2. Airflow Scheduler / Executor
3. Operators/ Tasks/ Sensors
4. Schedule/ Datasets/ Data Awareness
5. SubDags/ TaskGroups
6. XComs/ Variables/ Params
7. Dynamic DAG using Jinja Template 

**How to navigate through this Repo -**
1. Go to folder /main/ and open file airflow.docx
2. Go through the content of airflow.docx, this will provide detailed information on all the Airflow topics and path of the python code to follow.
3. For installation/ configurations, Follow markdown files or sh file present in each sub-folder of folder /main/install_and_config/
4. All python scripts can be found at /main/airflow-working-folder/dags
5. Jinja template scripts can be found at main/jinja-template
6. Additional scripts exist in the /main/ folder - 
    6.1. **/main/scripts.md**: Contains scripts to test Airflow tasks and accessing Airflow config file from Docker
    6.2. **/main/testTasksFunctions.py**: Python script to test API response which is used in Airflow Task present in /main/airflow-working-folder/dags/user-processing.py