from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


def tarnsform_task():
    with TaskGroup('transformGroup', tooltip="My transform task") as group:
        
        transform_a = BashOperator(
            task_id="transform_a",
            bash_command="sleep 1"
        )
        
        transform_b = BashOperator(
            task_id="transform_b",
            bash_command="sleep 4"
        )
        
        transform_c = BashOperator(
            task_id="transform_c",
            bash_command="sleep 1"
        )
        
        
    return group