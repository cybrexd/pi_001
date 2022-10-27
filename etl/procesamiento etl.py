import pandas as pd
import numpy as np
import os
import sqlalchemy
import pymysql
from sqlalchemy import create_engine


def ordenar_columnas(df):
    df = df[["precio","producto_id","sucursal_id"]]
    return(df)

def normalizar_id_sucursal(df):
    df["sucursal_id"] = df["sucursal_id"].str.split(" ",expand=True)[0]
    return(df)

def normalizar_id_producto(df):
    df['producto_id'] = df["producto_id"].astype(str).str.rstrip(".0")
    df['producto_id'] = df["producto_id"].str.zfill(13)
    charlen= len(df['producto_id'])
    string = (df['producto_id'])
    if (len(df['producto_id'])<13):
        df['producto_id']= "0"* (13-charlen)+df['producto_id']
    return(df)

def formatofecha(dataset):
    stringg = dataset
    return(stringg[15:19] + "-" + stringg[19:21] + "-" + stringg[21:23])

lista_dataset= os.listdir(r"datasets en formato correcto")


dftt = pd.DataFrame({'precio': [],
                   'producto_id': [],
                   'sucursal_id': [],
                   "fecha": [],},   
)


for dataset in lista_dataset:
    df = pd.DataFrame({'precio': [],
                   'producto_id': [],
                   'sucursal_id': [],
                   "fecha": [],},   
)
    df = pd.read_csv("datasets en formato correcto"+ "/"+dataset)
    df = ordenar_columnas(df)
    df["fecha"] = formatofecha(dataset)
    dftt= dftt.append(df,ignore_index=True)

dftt = normalizar_id_sucursal(dftt)
dftt = normalizar_id_producto(dftt)


dftt = dftt.dropna()


conexionstr = "mysql+pymysql://root:1234@localhost:3306/pi_01"

conexion = create_engine(conexionstr)

dbconexion = conexion.connect()

dftt.to_sql(name="precio_semana",con=conexion,if_exists="append",index=False)

