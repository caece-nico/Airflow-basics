from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime
import json


mi_dag = DAG(
                dag_id = 'obtiene_json', description='dag basico',
                start_date=datetime(2023,10,2),
                schedule_interval='1 * * * *',
                catchup = False 
)


def mi_check(a):
    print('ok')
    return True

def graba_json(b):
    with open('/opt/airflow/dags/mi_json.json','w') as f:
        f.write(b)
    return True

t_dummy = DummyOperator(task_id = 'task_1_dummy', dag=mi_dag)


test_api = HttpSensor(
                        task_id ='test_api',
                        http_conn_id = 'fakejsonconn',
                        endpoint = 'typicode/demo/posts',
                        response_check = lambda response : mi_check(response) ,
                        poke_interval = 5,
                        timeout = 20
)


mi_json = SimpleHttpOperator(
                                task_id = 'obtiene_data',
                                http_conn_id='fakejsonconn',
                                endpoint = 'typicode/demo/posts',
                                method = 'GET',
                                log_response = True,
                                dag = mi_dag,
                                response_filter = lambda response : graba_json(response.text)
)

t_dummy >> test_api >> mi_json