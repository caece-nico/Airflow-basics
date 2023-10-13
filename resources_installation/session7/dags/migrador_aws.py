from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.S3_hook import S3Hook
from airflow.sensors.filesystem import FileSensor

def f_error(context):
    print('huno un error')

dag = DAG(
            dag_id = 'migrador_aws', description = 'Migra datos de mi disco a aws s3',
            schedule_interval = '1 * * * *',
            start_date = datetime(2023,10,8),
            catchup=False
            )

dummy = DummyOperator(
                        task_id = 'no_hace_mada',
                        dag = dag
                        )

check_file = FileSensor(
                        task_id = 'Check_archivo',
                        filepath='/opt/airflow/dags/files',
                        poke_interval=5,
                        timeout=120,
                        on_failure_callback=f_error,
                        dag = dag
                        )

def f_copia_archivo(file_name, key, bucket_name):
    hook=S3Hook('airflows3conn')
    hook.load_file(filename=file_name, key=key, bucket_name=bucket_name)


copy_file = PythonOperator(
                            task_id = 'copia_s3',
                            python_callable=f_copia_archivo,
                            op_kwargs={
                                'file_name':'/opt/airflow/dags/files/customerdata.csv',
                                'key':'customerdata2.csv',
                                'bucket_name':'myairflowbucketnleali'
                                    },
                            dag = dag
                            )


dummy >> check_file >> copy_file