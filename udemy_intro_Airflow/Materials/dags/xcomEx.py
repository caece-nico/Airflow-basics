from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def _t1(ti):
    ti.xcom_push(key='my_key', value=[42, 3,5,6])
    
def _t2(ti):
    dato = ti.xcom_pull(key='my_key', task_ids = 't1')
    for d in dato:
        print(d)

with DAG(dag_id="xcom_example", start_date=datetime(2024,5,18),
         schedule_interval="@daily",
         catchup=False) as xcom_e:
    
    t1 = PythonOperator(
        task_id = "t1",
        python_callable=_t1
    )
    
    t2 = PythonOperator(
        task_id="t2",
        python_callable=_t2
    )
    
    
    
    t1 >> t2