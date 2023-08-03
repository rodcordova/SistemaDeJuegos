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
    return Anio

@app.get('/juegos/{Año}')  
def juegos(Anio: str):


    return Anio

@app.get('/generes/{Año}')  
def generes(Anio: str):
    return Anio


@app.get('/gov/{Año}')  
def gov(Anio: str):
    return Anio

@app.get('/asr/{Año}')  
def asr(Anio: str):
    return Anio