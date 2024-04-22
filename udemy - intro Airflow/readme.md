# Introduction to Airflow - Udemy

1. [Introduccion](#1.-Introduccion)
    - [Requisitos]()
    - [Core components]()


## 1. Introduccion

__¿Porque necesitamos Airflow?__

_Airflow_ nos permite manejar errores en nuestros Pipelines de forma eficiente y fácil.
POr ejemplo si tenemos un __Pipeline__ que consume, una API, carga con Snowflake y procesa con Dbt

![](./img/airflow_intro.png)

Con Airflow podemos capturar cualquier error es los pasos de este __Pipeline__ y determinar el curso de acción alternativo.

__¿Qué es Airlfow?__

Es una plataforma de codigo abierto para monitorear los workflows del data pipeline.
Permite __crear__, __monitorear__ y __esquedulear__ nuestros Workflows.

Tiene su porpia UI y permite crear nuestras propias Plug-in.

### Core components

Tiene un __web server__, un __Scheduler__ , un __metastore__ y un __triggerer__
Tambien tenemos el __executor__. El Executor no ejecuta tareas pero dice como se deben ejecutar. Por ejemplo si queremos ejecutar sobre Kubernetes, usamos el __Kubernetes Executor__ si queremos ejecutar en paralelo usamos __Cellery Executor__.

Cuando ejecutamos en paralelo tenemos dos componentes adicionales que son __Queue__ y __Worker__. Las tareas se van encolando en la   __Queue__ que serán tomadas por el __Worker__

![](./img/airflow_components.png)

__¿Que son los DAGs?__

Significa Directly Aciclic Graph. Compuesto por Aristas o Nodos, Edges y __sin Ciclos__.

![](./img/airflow_dag.png)

En este ejemplo vemos que __T1 T2 y T3__ son aristas o nodos (Task) que ejecutan en paralelo.
__T4__ tambien es un Nodo o Artista que depende de __T1 T2 y T3__. La dependencia se da por Edges.

__¿Que es un Operator?__

Un operador es una forma de encapsular lo que queremos hacer. 
Hay tres tipos.

|Tipo de operador|descripcion|ejemplo|
|----------------|-----------|-------|
|Action Operator|Ejecutan una función u Operacion|__PythonOperator__ o __BashOperator__|
|Transfer Operator|Pueden caer en desuso pero un ejemplo es para mover datos de MySQL a Redshift|__TransferOperator__|
|Sensor Operator|Se usan para esperar que algo ocurra antes de pasar a la siguiente tarea|__FileSensor__|


__¿Que es Task y Task Instance?__

Un operador es una __Tarea__ o __Task__ y cuando esto es ejecutado obtenemos un __Task Instance__

__¿Que es un Workflow?__

Es la combinacion de todos los conceptos anteriores.

![](./img/airflow_workflow.png)

### Requisitos

1. Necesitamos tener instalo Docker. 
2. Luego Nstalar Visual Studio Code.


