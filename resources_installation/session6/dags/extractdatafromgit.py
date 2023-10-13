from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime

dag_1 = DAG(dag_id = 'dag_simple_http', description = 'This dag extract data from github',
            schedule_interval = '1 * * * *', 
            start_date=datetime(2023,10,3), catchup=False
            )

def mi_respuesta(a):
    print('Ok')
    return True

def my_funcion():
    print('Hola')

def to_csv(a):
    dd = '/opt/airflow/dags/mi_archivo.csv'
    with open(dd,'w') as file:
        file.write(a)
    return True

checkapi = HttpSensor(
                        task_id = 'Check_ip',
                        http_conn_id = 'gitconn',
                        endpoint = 'caece-nico/Airflow-basics/master/resources_installation/session5/customer.csv',
                        response_check= lambda response : mi_respuesta(response),
                        poke_interval=5,
                        timeout = 20,
                        dag = dag_1
                        )

getcustoerdata = SimpleHttpOperator(

                                        task_id = 'getdata',
                                        method = 'GET',
                                        http_conn_id='gitconn',
                                        endpoint='caece-nico/Airflow-basics/master/resources_installation/session5/customer.csv',
                                        response_filter=lambda response: to_csv(response.text),
                                        log_response=True,
                                        dag = dag_1
)


task_1 = DummyOperator(task_id='No_hace_nada', dag=dag_1)

task_2 = PythonOperator(task_id ='segundo', python_callable=my_funcion, dag=dag_1)

task_1 >> task_2 >> checkapi >> getcustoerdata