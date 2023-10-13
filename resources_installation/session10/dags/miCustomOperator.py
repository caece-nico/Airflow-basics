from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

def mi_funcion():
    print('Hola')
    return True


mi_dag = DAG(dag_id = 'muevo_s3_a_s3', description = 'Ejemplo para mover de un bucket a otro',
schedule_interval='1 * * * *', start_date=datetime(2023,10,12),
catchup = False)


no_hace_nada = BashOperator(task_id='inicio_task', bash_command="sleep 2", dag=mi_dag)

muestra_por_pantalla = PythonOperator(task_id = 'segunda_task', python_callable=mi_funcion,dag=mi_dag)


no_hace_nada >> muestra_por_pantalla