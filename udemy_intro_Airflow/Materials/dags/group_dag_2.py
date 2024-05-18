from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from datetime import datetime
from subdags.subdag_downloads import subdag_download

with DAG(dag_id='group_dag_grouped', start_date=datetime(2024,5,18),
         schedule_interval='@daily',
         catchup=False) as dag:
    
    args = {'start_date':dag.start_date,
            'schedule_interval':dag.schedule_interval,
            'catchup':dag.catchup}
    
    downloads = SubDagOperator(
        task_id='downloads',
        subdag=subdag_download(dag.dag_id, 'downloads', args)
    )
    
    checkfile = BashOperator(
        task_id = 'Checkfile',
        bash_command='sleep 10'
    )
    
    load_a = BashOperator(
        task_id='load_a',
        bash_command='sleep 5'
    )
    

    load_b = BashOperator(
        task_id='load_b',
        bash_command='sleep 5'
    )
    

    load_c = BashOperator(
        task_id='load_c',
        bash_command='sleep 5'
    )
    
    
    downloads >> checkfile >> [load_a, load_b, load_c]