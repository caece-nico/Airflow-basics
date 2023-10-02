from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

mi_dag = DAG('second_dag', description = 'Este es mi segundo DAG',
        schedule_interval='1 * * * *',
        start_date=datetime(2023,10,1), 
        catchup=False)

def welcomeStudents():
    print('Welcome to this tuto')

mi_task_1 = DummyOperator(task_id='first_dag_task', dag = mi_dag)


mi_task_2 = PythonOperator(
                            task_id='second_dag_task', 
                            python_callable=welcomeStudents,
                            dag=mi_dag)

mi_task_1 >> mi_task_2