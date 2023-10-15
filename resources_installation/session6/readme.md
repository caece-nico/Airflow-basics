# Docker-compose & Airflow

- Tabla de contenido

1. [Introduccion](#Introduccion)
2. [Requisitos](#Requisitos)
    - [Dockerfile](#Dockerfile)
    - [Airflow_commands.sh](#Airflow_commands.sh)
    - [gitignore](#gitignore)
3. [Docker-compose](#Docker-compose)
4. [Ejecucion](#Ejecucion)
5. [Importante-AWS](#Importante-AWS)
6. [IP-Docker-compose](#IP-Docker_compose)

## Introduccion

A medida que incorporamos nuevos servicios como bases de datos + python es necesario migrar de contenedores de docker a docker-compose. Esto hace que el manejo de redes sea mas fácil al igual que la creación de volumenes.

## Requisitos

La estructura de archivos debe ser:

```
../..
    |_ Python
        |-airflow_commands.sh
        |-Dockerfile
    |_ mssql
        |-Dockerfile
    |_ mi_data
    |_ dags
    - .gitignore
    - docker-compose
```

## Dockerfile

- Airflow

```docker
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

#Instalamos el providers para mysql y amazon
RUN apt-get update && apt-get install -y \
  default-libmysqlclient-dev \
  pkg-config \
  gcc \
  pkg-config \
  && rm -rf /var/lib/apt/lists/*
  
RUN pip install 'apache-airflow[mysql]'
RUN pip install 'apache-airflow[amazon]'

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


- Mysql

```docker
FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD='sa'
ENV MYSQL_DATABASE='sa'
ENV MYSQL_USER = 'user'
ENV MYSQL_PASS = 'pass'
```

## - gitignore

El .gtignore es muy importante, acá indicamos lo que no queremos que se haga commit.
En este caso no queremos committear lo que está en el directorio mi_data porque este directorio en un volumen donde se guarda toda la base de datos.

```git
mi_data/
```

## 3. Docker-compose

```Docker

services:
  mysql:
    build: ./myssql/
    volumes:
      - ./mi_data:/var/lib/mysql
    ports:
      - '3306:3306'


  airflow:
    build: ./airflow/
    volumes:
      - ./dags:/opt/airflow/dags
    ports:
      - 8888:8080
```

## 4. Ejecucion

Para ejecutar un conjunto de contenedores en un docker ejecupamos el siguiente comando en el directorio donde se encuentra el archivo.

```docker
docker-compose up .
```
## Importante-AWS

- Al archivo dockerfile de __AIRFLOW__ es importante agregarle estas lineas despues de __RUN PIP INSTALL__
para agregar los paquetes necesarios para crear las conecciones a AWS y MYSQL sino no funciona.

```docker
#Instalamos el providers para mysql y amazon
RUN apt-get update && apt-get install -y \
  default-libmysqlclient-dev \
  pkg-config \
  gcc \
  pkg-config \
  && rm -rf /var/lib/apt/lists/*
  
RUN pip install 'apache-airflow[mysql]'
RUN pip install 'apache-airflow[amazon]'
```

## IP-Docker_compose

Para encontrar la IP de un servicio iniciado en un contenedor lo que debemos hacer es.

1. Buscar en contenedor al que quremos acceder.

```docker
docker ps
```

2. Ejecutra el comando Docker sobre ese contenedor.

```docker
docker inspect id_contenedor
```

- Si nos conectamos localmente desde nuestra pc a un contenedor usamos localhost:puerto
- Si nos conectamos desde otro contenedor usamos la ip que muestra __DOCKER INSPECT__