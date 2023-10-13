from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator

def f_procesa_baco_maco(ti):
    dato = 200
    ti.xcom_push(key='Total_registros', value=dato)
    return True


def f_procesa_banco_bbva(ti):
    dato = 500
    ti.xcom_push(key='Total_registros', value=dato)
    return True


def f_check(ti):
    transaccion_1 = ti.xcom_pull(key='Total_registros', task_ids=['procesa_datos_bco_macro'])
    transaccion_2 = ti.xcom_pull(key='Total_registros', task_ids=['procesa_datos_bco_bbva'])
    if transaccion_1[0] +  transaccion_2[0] > 200:
        return 'envia_mail'
    else:
        return 'muestra_por_pantalla'
    return True

def muestra_por_pantalla_fdx():
    print('NO HAY NECESIDAD DE MOSTRAR NADA')
    return True

dag = DAG(
            dag_id = 'ejemplo_xcom_mails_branch', description = 'Xcom y branch operator con email',
            schedule_interval = '1 * * * *',
            start_date = datetime(2023,10,8),
            catchup=False
            )

descarga_bco_macro = BashOperator(
                    task_id = 'descarga_datos_bco_macro',
                    bash_command='sleep 2;',
                    dag = dag
                    )

descarga_bco_bbva = BashOperator(
                    task_id = 'descarga_datos_bco_bbva',
                    bash_command='sleep 2;',
                    dag = dag
                    )

process_data_1 = PythonOperator(
                                task_id = 'procesa_datos_bco_macro', 
                                python_callable=f_procesa_baco_maco, 
                                dag=dag)

process_data_2 = PythonOperator(
                                task_id = 'procesa_datos_bco_bbva',
                                python_callable = f_procesa_banco_bbva,
                                dag = dag)

check_data = BranchPythonOperator(
                            task_id = 'check_data',
                            python_callable=f_check,
                            dag=dag)

envia_mail = EmailOperator(
                            task_id='envia_mail',
                            to='leali.nicolas@hotmail.com',
                            subject='Alerta',
                            html_content='Esta es una alerta automatica',
                            dag=dag)

muestra_por_pantalla = PythonOperator(
                                        task_id='muestra_por_pantalla',
                                        python_callable=muestra_por_pantalla_fdx,
                                        dag=dag
                )


descarga_bco_macro >> process_data_1 >> check_data>>[envia_mail, muestra_por_pantalla]
descarga_bco_bbva >> process_data_2 >> check_data>>[envia_mail, muestra_por_pantalla]