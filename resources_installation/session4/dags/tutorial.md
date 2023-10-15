# Introducción __OPERADOR PYTHON__

```python
from airflow.operators.python import PythonOperator
```

## Importante

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
