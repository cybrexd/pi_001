# PI 01

En Este repositorio se encuentran los archivos necesarios para realizar un proceso de etl y una carga incremental hacia una DB de MYsql,transformandolos y normalizandolos para ser cargados adecuadamente.


# Programas utilizados 

MySql Workbench: Crear DB y realizar las queries o consultas
Python (incluyendo las librerias Pandas,sqlalchemy) : El script que ejecuta y engloba todo proceso de etl esta basado en python,el cual nos permite trabajar con librerias muy utiles.Todo el proceso de conversion de formatos, limpieza de datos y joins se realiza utiliza la libreria Pandas. La conexion entre el script y la db, y la posterior carga incremental se hace atravez de sqlalchemy.


# Funcionamiento 

1- Instalar las librerias necesarias de python "Pandas" y "sqlalchemy" utilizando el comando pip install.
2- Transformar los formatos datasets que se quieren cargar en la DB a csv utilizando Pandas(manteniendo el separador en "," y el encoding en "utf-16", Guardandolos en la carpeta "datasets en formato correcto"
3- Ejecutar el script procesamiento etl.py, el cual cargara los datasets de la carpeta, los unira y normalizara y luego enviara a la DB

# Flujo de Datos

