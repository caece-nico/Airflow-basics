from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

from datetime import datetime

def _t1 (ti):
    ti.xcom_push(key='key_t1', value = 34)

def _t2(ti):
    valor = ti.xcom_pull(key='valor_interno_branch', task_ids='brancherWithTrigger')
    print(valor)
    
def _t3(ti):
    valor = ti.xcom_pull(key='valor_interno_branch', task_ids='brancherWithTrigger')
    print(valor)
    
def _t4():
    print('Esta es la tarea final, no hace nada')

def _brancher(ti):
    valor = ti.xcom_pull(key='key_t1', task_ids='t1')
    ti.xcom_push(key='valor_interno_branch', value = [23,45,67])
    if valor >= 56:
        return 't2'
    return 't3'

with DAG(dag_id = 'myBranchWithTrigger', start_date = datetime(2024,5,18), 
         schedule_interval="@daily",
         catchup=False) as dag:
    
    
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
    
    t2 = PythonOperator(
        task_id = 't2',
        python_callable=_t2
    )
    
    brancher = BranchPythonOperator(
        task_id = 'brancherWithTrigger',
        python_callable= _brancher
    )
    
    t3 = PythonOperator(
        task_id = 't3',
        python_callable=_t3
    )
    
    t4 = PythonOperator(
        task_id='t4',
        python_callable=_t4,
        trigger_rule='none_failed_min_one_success'
    )
    
    t1 >> brancher >> [t2, t3] >> t4
    