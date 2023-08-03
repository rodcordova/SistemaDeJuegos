from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json
import numpy as np
import ast

app = FastAPI()

df = pd.read_csv("Dataset/ds_clean.csv")

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
    return Anio
