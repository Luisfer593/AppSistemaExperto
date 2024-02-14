import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_selection import SelectFromModel
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from joblib import dump
from config.db_config import db_connection_pool
from mysql.connector import Error

def cargar_datos_desde_bd():
    try:
        # Obtener una conexión de la base de datos
        connection = db_connection_pool.get_connection()

        # Consulta SQL para obtener datos
        consulta = "SELECT * FROM solicitudes_credito"

        # Obtener datos desde la base de datos
        datos = pd.read_sql(consulta, connection)

        return datos

    except Error as e:
        print("Error al cargar datos desde la base de datos:", e)

    finally:
        # Cerrar la conexión
        if connection:
            connection.close()

# Cargar datos desde la base de datos
datos = cargar_datos_desde_bd()

# Preprocesamiento de datos
datos.drop(['id', 'nombre', 'apellido'], axis=1, inplace=True)  # Elimina las columnas no relevantes
datos_encoded = pd.get_dummies(datos, columns=['historial_crediticio', 'ingresos_deudas'])

# Dividir el conjunto de datos en características (X) y el objetivo (y)
X = datos_encoded.drop('cumple_normativas', axis=1)
y = datos_encoded['cumple_normativas']

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline para preprocesamiento y entrenamiento del modelo
pipeline = Pipeline([
    ('scaling', StandardScaler()),  # Escala las características numéricas
    ('feature_selection', SelectFromModel(RandomForestClassifier())),  # Selección de características
    ('sampling', SMOTE()),  # Manejo del desequilibrio de clases
    ('model', RandomForestClassifier())  # Modelo RandomForest
])

# Parámetros para la búsqueda en cuadrícula de RandomForest
param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [None, 10],
    'model__min_samples_split': [2, 5],
    'model__min_samples_leaf': [1]
}

# Búsqueda en cuadrícula para ajuste de hiperparámetros
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Mejores parámetros encontrados
print("Mejores parámetros:", grid_search.best_params_)

# Mejor modelo después de la búsqueda en cuadrícula
mejor_modelo = grid_search.best_estimator_

# Evaluación del modelo en el conjunto de prueba
precision = mejor_modelo.score(X_test, y_test)
print("Precisión del modelo en el conjunto de prueba:", precision)

# Guardar el modelo entrenado
dump(mejor_modelo, 'modelo_entrenado.joblib')
