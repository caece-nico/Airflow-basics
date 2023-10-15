# Introducción a __AIRLFOW__

1. [Introduccion](#Introduccion)
2. [Operadores](#Operadores)
    - [DummyOperator](#DummyOperator)
    - [PythonOperator](#PythonOperator)
    - [BashOperator](#BashOperator)

## Introduccion

- ¿Qué es un DAG? 

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

## Operadores

### DummyOperator

```python
task_1 = DummyOperator(
                        task_id=,
                        dag=...
                        )
```


### Ejecucion

task_1


## PythonOperator

```python
from airflow.operators.python import PythonOperator
```

### Importante

El operador de Python llama a una funcion que puede estar declara en el mismo .py o en otro archivo.

```python
def mi_funcion_python():
    print('Mi primer funcion\n')
    return True

dag = DAG (
            dag_id=
            ...
            )

task_1 = PythonOperator(
                            task_id = ''
                            python_callable=mi_funcion_python
                            dag = 
)
```
