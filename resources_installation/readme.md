# Airflow Initial

## Cómo ejecutar este proyecto en Docker y Docker Compose.


1. [Requisitos](#Requisitos)
1. [Airlfow](#Airflow)
    - [Dockerfile](#Dockerfile)
    - [airflow_command.sh](#airflow_command.sh)
2. [Ejecución](#Ejecucion)
3. [Importante](#Importante)

## Requisitos

- En el directorio deben existir los archivos Dockerfile y airflow_commands.sh 

## 1.a Dockerfile

Para Ejecutar una imagen en Docker primero creamos el archivo Dockerfile para instalar Python -> las bibliotecas necesarias de Airflow y luego Airflow. Tambien ejecuta el archivo __airflow_commandas.sh__ que inicializa variablkes necesarias de Airflow.



```Docker
#base image
FROM python:3.8-slim

LABEL maintainer="Sourabh"

#arguments
ARG AIRFLOW_VERSION=2.5.1
ARG PYTHON_VERSION=3.8
ARG AIRFLOW_HOME=/opt/airflow 

ENV AIRFLOW_HOME=${AIRFLOW_HOME}

#install libraries

# Install dependencies and tools
RUN apt-get update -yqq && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \ 
    wget \
    libczmq-dev \
    curl \
    libssl-dev \
    git \
    inetutils-telnet \
    bind9utils freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    libffi-dev libpq-dev \
    freetds-bin build-essential \
    default-libmysqlclient-dev \
    apt-utils \
    rsync \
    zip \
    unzip \
    gcc \
    vim \
    locales \
    && apt-get clean

RUN wget https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.8.txt


RUN pip install --upgrade pip && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} azurelib && \
    pip install apache-airflow[postgres]==${AIRFLOW_VERSION} --constraint /constraints-3.8.txt

# Copy the airflow_init.sh from host to container (at path AIRFLOW_HOME)
COPY ./airflow_commands.sh ./airflow_commands.sh

# Set the airflow_init.sh file to be executable
RUN chmod +x ./airflow_commands.sh

# Set the owner of the files in AIRFLOW_HOME to the user airflow
RUN chown -R azurelib: ${AIRFLOW_HOME}

# Set the username to use
USER azurelib

# Set workdir (it's like a cd inside the container)
WORKDIR ${AIRFLOW_HOME}

#create dags directory
RUN mkdir dags

# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080

# Execute the airflow_commands.sh
ENTRYPOINT [ "/airflow_commands.sh" ]
```

## airflow_commands.sh

- Este archivo crea el usuario con el que nos vamos a loggear en localhost:8080 e inicializa los servicios.

```bash
#!/usr/bin/env bash

# Initiliase the metastore
airflow db init

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Create user
airflow users create -u azurelib -p azurelib -r Admin -e nleali88@gmail.com -f Sourabh -l Sahu

# Run the web server in foreground (for docker logs)
exec airflow webserver
```


## Ejecucion

- Creamos la imagen

```docker
docker build . (directorio_actual) -t (nombre_imagen)
```

- Ejecutamos la imagen

```docker
docker run -it -p 8888:8080 -v d:\..\.. : /opt/airflow/dag id_imagen
```

- vemos que contenedores estan corriendo

```docker
docker ps
```

- entramos a un contenedor

```docker
docker exec -it id_contenedor /bin/bash
```

## Importante

Ver documentación de ejecución a partir de la clase 6 con Docker-compose para usar bases de datos.