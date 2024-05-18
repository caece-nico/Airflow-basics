from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def download_task():
    
    with TaskGroup("downloadsGroup", tooltip="Download task") as group:
        
        download_a = BashOperator(
            task_id = "Download_a",
            bash_command= "sleep 10"
        )
        
        download_b = BashOperator(
            task_id="download_b",
            bash_command="sleep 20"
        )
        
        download_c = BashOperator(
            task_id = "download_c",
            bash_command="sleep 2"
        )      
        
    return group