from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor

def test_con(e):
    print(e)
    return True


dag = DAG(
            dag_id='dag_api_http', description ='Traemos un archivo .csv de internet',
            schedule_interval='1 * * * *', 
            start_date=datetime(2023,10,1),
            catchup=False
            )

test_operator = DummyOperator(task_id='dag_test_task', dag=dag)


ceckapi = HttpSensor(
                        task_id='fetch_customer_data',
                        http_conn_id='githubconn',
                        endpoint='/caece-nico/Airflow-basics/master/resources_installation/session5/customer.csv',
                        response_check=lambda response: test_con(response.text),
                        poke_interval=5,
                        timeout=20
)

test_operator >> ceckapi