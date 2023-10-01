from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


dag = DAG('dag_testing_feb', description='Hello World DAG',
          schedule_interval='0 * * * *',
          start_date=datetime(2023, 1, 11), catchup=False)

test_operator = DummyOperator(task_id='dag_test_task', dag=dag)

test_operator


