from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

dag_1 = DAG(
            dag_id = 'bash_dag_example', description = 'Ejemplo de dag para la session 5 - bash',
            schedule_interval = '1 * * * *',
            start_date=datetime(2023,10,2), catchup = False
            )

def mifuncion(dato='nicolas'):
    print('Este es un mensaje para {}'.format(dato))

mi_task = BashOperator(task_id = 'first_bash_task', bash_command="echo hola", dag = dag_1)

mi_python = PythonOperator(task_id='Second_dag_task', python_callable=mifuncion,dag=dag_1 )


mi_task >> mi_python