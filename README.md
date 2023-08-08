# Steam ML Project README

Este repositorio contiene el código y la documentación necesaria para abordar el desafío de crear un modelo de predicción de precios de videojuegos para Steam. El objetivo principal es desarrollar un modelo efectivo y una API para la predicción de precios basados en diferentes características de los juegos. El proyecto se enfoca en el ciclo de vida completo de un proyecto de Machine Learning, desde la manipulación y exploración de datos hasta la implementación de un modelo de predicción y la creación de una API para interactuar con el modelo.

## Contexto y Rol

Este proyecto aborda el desafío de predecir el precio de los videojuegos en la plataforma Steam. Como Data Scientist en Steam, Nuestra tarea es desarrollar un modelo de predicción efectivo a partir de datos inicialmente no tratados y crear una API que permita a otros departamentos utilizar este modelo para predecir precios.

## Estructura del Repositorio

- `datasets/`: Contiene los datos originales y datos tranformados en el ETL y EDA.

## Instrucciones de Uso

1. **Exploración de Datos (EDA)**: Los Jupyter Notebooks contienen el análisis exploratorio de datos. 

2. **Preprocesamiento y Modelado**: Los Jupyter Notebooks también contienen el preprocesamiento de datos y la creación del modelo de predicción. 

3. **API**: el archivo main.py contiene el código fuente de la API. Ejecute la API utilizando el framework FastAPI siguiendo las instrucciones en el archivo correspondiente.

## API Endpoints

- `/genero`: Proporciona una lista con los 5 géneros más ofrecidos en un año determinado.
- `/juegos`: Devuelve una lista con los juegos lanzados en un año.
- `/specs`: Ofrece una lista con los 5 specs más comunes en un año.
- `/earlyacces`: Devuelve la cantidad de juegos lanzados en un año con early access.
- `/sentiment`: Proporciona una lista con el análisis de sentimiento según el año de lanzamiento.
- `/metascore`: Devuelve los 5 juegos con el mayor metascore en un año.

## Conclusiones

Este proyecto aborda el proceso completo de un proyecto de Machine Learning, desde la manipulación de datos hasta la implementación de un modelo de predicción y la creación de una API. A lo largo del proyecto, se enfatiza la importancia de un sólido Análisis Exploratorio de Datos (EDA) para comprender y procesar adecuadamente los datos, así como la implementación efectiva de modelos de predicción para abordar problemas de negocio.
