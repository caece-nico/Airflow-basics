# Introducción a __AIRLFOW__

1. ¿Qué es un DAG?

Directly Acyclic Graph. Está formado por dags y tareas.

librerias importantes

```python
from  datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
```

## Declaracion de un dag 

```python
xx = DAG(
        dag_id=
        description=
        schedule_interval='* * * * *'
        start_date=datetime()
        catchup=False # se usa para ejecutar lo que no corrio
        )
```

## creamos una tarea

```python
task_1 = DummyOperator(
                        task_id=,
                        dag=...
                        )
```


## Ejecucion

task_1