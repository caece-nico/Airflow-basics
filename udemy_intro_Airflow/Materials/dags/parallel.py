from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="parallel_example",
    schedule="@daily",
    start_date=datetime(2024,5,1),
    catchup=False) as dag:
    
    extract_a = BashOperator(
        task_id='extract_a',
        bash_command="sleep 10"
    )
    
    load_a = BashOperator(
        task_id="load_a",
        bash_command="sleep 10"
    )
    
    extract_c = BashOperator(
        task_id="extract_c",
        bash_command="sleep 10"
    )
    
    load_c = BashOperator(
        task_id="load_c",
        queue = 'high_cpu',
        bash_command="sleep 30"
    )
    
    transform = BashOperator(
        task_id="transform",
        bash_command="sleep 10"
    )
    
    extract_a >> load_a
    extract_c >> load_c
    [load_a, load_c] >> transform