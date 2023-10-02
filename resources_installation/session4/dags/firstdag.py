from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('first_dag', description='This is my first dag',
            schedule_interval='1 * * * *',
            start_date = datetime(2023,10,1), catchup=False)


firsttask = DummyOperator(task_id='first_dag_task', dag=dag)

firsttask