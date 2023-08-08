from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json
import numpy as np
import ast
from model import modelo_predict

app = FastAPI()

df = pd.read_csv("Datasets/ds_clean.csv")

@app.get('/genero/{Año}')  
def genero(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]
    
    # Llevo en lista literal ya que al traerlo esta en string y ademas los nan no los itero
    filtrada['genres'] = filtrada['genres'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else np.nan)

    # Llevar todos los elementos de la columna a una sola lista
    lista_categorias = [item for row in filtrada['genres']  if isinstance(row, list)  for item in row]

    # Contar la cantidad de ocurrencias de cada elemento utilizando un diccionario
    category_counts = {}
    for category in lista_categorias:
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Ordeno y saco el top 5
    top_5_categories = sorted(category_counts, key=lambda category: category_counts[category], reverse=True)[:5]

    # Empaqueto la respuesta en un diccionario
    respuesta={'Top_5_generos':top_5_categories}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get('/juegos/{Año}')  
def juegos(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]

    # Llevar todos los elementos de la columna a una sola lista
    lista_juegos = [item for item in filtrada['app_name']  if isinstance(item, str)  ]

    # Empaqueto la respuesta en un diccionario
    respuesta={'lista_juegos':lista_juegos}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get('/specs/{Año}')  
def specs(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]
    
    # Llevo en lista literal ya que al traerlo esta en string y ademas los nan no los itero
    filtrada['specs'] = filtrada['specs'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else np.nan)

    # Llevar todos los elementos de la columna a una sola lista
    lista_specs = [item for row in filtrada['specs']  if isinstance(row, list)  for item in row]

    # Contar la cantidad de ocurrencias de cada elemento utilizando un diccionario
    category_counts = {}
    for category in lista_specs:
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Ordeno y saco el top 5
    top_5_categories = sorted(category_counts, key=lambda category: category_counts[category], reverse=True)[:5]

    # Empaqueto la respuesta en un diccionario
    respuesta={'top_5_categories':top_5_categories}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get('/earlyacces/{Año}')  
def earlyacces(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]
    
    # Llevar todos los elementos de la columna a una sola lista
    lista_early = [item for item in filtrada['early_access']  if isinstance(item, bool)  ]

    # Contar la cantidad de ocurrencias de cada elemento utilizando un diccionario
    early_counts = {}
    for category in lista_early:
        early_counts[category] = early_counts.get(category, 0) + 1

    # Empaqueto la respuesta en un diccionario
    respuesta={'cantidad en true': early_counts[True]}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get('/sentiment/{Año}')  
def sentiment(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]

    # Llevar todos los elementos de la columna a una sola lista
    lista_sentiment = [item for item in filtrada['sentiment']  if isinstance(item, str)  ]

    # Contar la cantidad de ocurrencias de cada elemento utilizando un diccionario
    category_counts = {}
    for category in lista_sentiment:
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Empaqueto la respuesta en un diccionario
    respuesta={'sentiment': category_counts}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get('/metascore/{Año}')
def metascore(Anio: str):
    # Filtro por el anio
    filtrada=df[df['release_year']==int(Anio)]

    # Ordenamos de forma desendente
    ordenados=filtrada.sort_values('metascore',ascending=False)

    # Llevar todos los elementos de la columna a una sola lista
    lista_juegos = [item for item in ordenados['app_name']  if isinstance(item, str) ]

    # Empaqueto la respuesta en un diccionario
    respuesta={'lista_juegos': lista_juegos[:5]}

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")

    return response


@app.get("/modelo de prediccion")
def prediccion(
    genres:str,
    release_year:int ,
    metascore:int,
    app_name:str ):

    respuesta=modelo_predict(genres,release_year,metascore,app_name)

    # Convertimos el diccionario a JSON
    json_data = json.dumps(respuesta, indent=4)
    response = Response(content=json_data, media_type="application/json")
    return response
