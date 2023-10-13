from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python   import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.hooks.mysql_hook import MySqlHook
import json

dag_1 = DAG(
            dag_id = 'Ejemplo_mysql', description = 'Primer dag para llamar a mysql',
            schedule_interval = '1 * * * *',
            start_date = datetime(2023,10,5), catchup = False
)

drop_table_if_exists = MySqlOperator(
    task_id ='drop_table',
    mysql_conn_id='mysqlconn',
    sql = r"""
    DROP TABLE IF EXISTS Post;
    """,
    dag=dag_1
)


create_table_mssql_task = MySqlOperator(
    task_id='create_table',
    mysql_conn_id = 'mysqlconn',
    sql = r"""
    CREATE TABLE Post(
        post_id int,
        post text
    );
    """,
    dag = dag_1
)


@dag_1.task(task_id='Insert_post_mysqlhook')
def insert_mysql_hook():
    mysql_hook = MySqlHook(mysql_conn_id='mysqlconn', schemma='sa' )
    with open('/opt/airflow/dags/mi_json.json','r') as f:
        data = f.read()
        djson = json.loads(data)
        dlist = []
        for items in djson:
            dlist.append((items['id'],items['title']))
        target_field = ['post_id','post']
        mysql_hook.insert_rows(table='Post', rows=dlist,target_fields=target_field)



drop_table_if_exists >> create_table_mssql_task >> insert_mysql_hook()