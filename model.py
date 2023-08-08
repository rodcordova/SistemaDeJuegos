import pandas as pd
import nltk
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from mlxtend.regressor import StackingRegressor
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import ast

df = pd.read_csv("Datasets/data_reducida.csv")

df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else np.nan)
df['genres']= df['genres'].apply(lambda x:x[0] )
# Utiliza el método .head() para seleccionar los primeros 1000 datos
df2 = df.head(2515)

# Generar una nube de palabras y extraer características
def extract_word_features(texts):
    stop_words = set(stopwords.words('english'))
    combined_text = ' '.join(str(text) for text in texts)
    words = word_tokenize(combined_text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    freq_dist = nltk.FreqDist(filtered_words)
    
    # Devuelve la frecuencia de palabras clave relevantes
    return freq_dist['keyword1'], freq_dist['keyword2'], ...

def modelo_predict(
    genres:str,
    release_year:int ,
    metascore:int,
    app_name:str ):
    
    # Dividir datos en características (X) y objetivo (y)
    X = df2[["genres", "release_year", "metascore"]]
    y = df2["price"]

    # Obtener las características de las nubes de palabras para los nombres de los juegos
    word_features = extract_word_features(df2['app_name'])

    # Agregar las características al DataFrame
    df2['keyword1_freq'] = word_features[0]
    df2['keyword2_freq'] = word_features[1]
    ...

    # Codificar variables categóricas usando One-Hot Encoding
    encoder = OneHotEncoder(sparse=False)
    X_encoded = encoder.fit_transform(X[["genres"]])

# Combinar características numéricas y codificadas
    X_final = pd.concat([X[["release_year", "metascore"]], pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(["genres"]))], axis=1)

# Dividir datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2, random_state=42)

# Crear modelos base
    model_rf = RandomForestRegressor(random_state=42)
    model_gb = GradientBoostingRegressor(random_state=42)
    model_lr = LinearRegression()

# Crear ensamble con stacking
    stacking_regressor = StackingRegressor(regressors=[model_rf, model_gb, model_lr], meta_regressor=LinearRegression())

# Crear pipeline
    pipeline = Pipeline(steps=[("stacking", stacking_regressor)])

# Entrenar el modelo
    pipeline.fit(X_train, y_train)

# Realizar predicción para los valores dados
    input_data = {
        "genres": [genres],
        "release_year": [release_year],
        "metascore": [metascore],
        "app_name": [app_name]  # Agregar el nombre del nuevo juego
    }

    input_df = pd.DataFrame(input_data)
    word_features_input = extract_word_features(input_df['app_name'])
    input_df['keyword1_freq'] = word_features_input[0]
    input_df['keyword2_freq'] = word_features_input[1]
    ...

    input_encoded = encoder.transform(input_df[["genres"]])
    input_final = pd.concat([input_df[["release_year", "metascore"]], pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(["genres"]))], axis=1)

    predicted_price = pipeline.predict(input_final)[0]

# Calcular RMSE para las predicciones de prueba
    predictions = pipeline.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    return {"Precio Predicho:": predicted_price,"RMSE en el Conjunto de Prueba:": rmse}
