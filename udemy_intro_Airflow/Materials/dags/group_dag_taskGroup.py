from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.group_download import download_task
from groups.group_transform import tarnsform_task

from datetime import datetime

with DAG(dag_id="TaksGrouped_dag", start_date=datetime(2024,5,18), 
         schedule_interval="@daily", 
         catchup=False) as dag:
    
    
    downloads = download_task()
    
    checkfile = BashOperator(
        task_id = "checkFile",
        bash_command="sleep 2"
    )

    transform = tarnsform_task()
    
    
    downloads >> checkfile >> transform