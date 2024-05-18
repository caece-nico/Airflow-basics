from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

from datetime import datetime


def _t1(ti):
    ti.xcom_push(key='mi_clave', value=[1,0])

def _t2(ti):
    print('Se ha ejecutado la tarea t2')
    final = ti.xcom_pull(key='clave_branch', task_ids='branchOp')
    print(final)

def _t3(ti):
    print('se ha ejecutado la tarea t3')

def _branch(ti):
    value = ti.xcom_pull(key='mi_clave', task_ids='t1')
    ti.xcom_push(key='clave_branch', value=[987,789])
    if value[0] == 1:
        return 't2'
    return 't3'

with DAG(dag_id='myBranchDag', start_date=datetime(2024,5,18),
         schedule_interval="@daily",
         catchup=False) as dag:
    
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
    
    branch = BranchPythonOperator(
        task_id = 'branchOp',
        python_callable=_branch
        
    )
    
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )
    
    t3 = PythonOperator(
        task_id='t3',
        python_callable=_t3
    )


    t1 >> branch >> [t2, t3]