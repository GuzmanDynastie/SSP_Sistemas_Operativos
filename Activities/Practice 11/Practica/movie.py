import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

path = './Activities/Practice 11/CSV/movies.csv'
new_path = './Activities/Practice 11/CSV/new_movies.csv'

class Movies:
    def __init__(self, path):
        self.path = path
        self.replaced_with_zeros = None
        self.read_csv()
        
    def read_csv(self):
        self.movie_df = pd.read_csv(self.path)
        self.clean_data()
        
    # Defino un método para limpiar los datos del DataFrame.
    def clean_data(self):
        # Selecciono las columnas numéricas del DataFrame.
        numeric_columns = self.movie_df.select_dtypes(include=[np.number]).columns
        # Guardo la cantidad de valores nulos en las columnas numéricas.
        self.replaced_with_zeros = self.movie_df[numeric_columns].isna().sum()
        # Reemplazo los valores nulos con 0 en las columnas numéricas.
        self.movie_df[numeric_columns] = self.movie_df[numeric_columns].fillna(0)
    
    # Defino un método para entrenar un modelo de regresión y hacer predicciones.
    def train_and_predict(self):
        # Codifico las características categóricas usando one-hot encoding.
        data_encoded = pd.get_dummies(self.movie_df)
        # Guardo una copia de las columnas reemplazadas con 0.
        columns_with_zeros = self.replaced_with_zeros[self.replaced_with_zeros > 0].index.tolist()
        # Divido los datos en características (X) y la variable objetivo (y).
        X = data_encoded.drop(columns=['ventas'])  # Características
        y = data_encoded['ventas']  # Variable objetivo
        # Divido los datos en conjunto de entrenamiento y conjunto de prueba.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Estandarizo las características.
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        # Inicializo el modelo de regresión Ridge.
        alpha = 1.0  # Factor de regularización
        model = Ridge(alpha=alpha)
        # Entreno el modelo.
        model.fit(X_train_scaled, y_train)
        # Realizo predicciones en el conjunto de prueba.
        y_pred = model.predict(X_test_scaled)
        # Agrego una columna de predicciones al conjunto de datos original.
        self.movie_df['ventas_pred'] = model.predict(scaler.transform(X))
        # Guardo las columnas reemplazadas con 0 junto con las predicciones.
        columns_to_save = columns_with_zeros + ['ventas_pred']
        self.movie_df.to_csv(new_path, index=False)

if __name__ == '__main__':
    movies = Movies(path)
    movies.train_and_predict()