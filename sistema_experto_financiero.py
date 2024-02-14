from flask import Flask, request, render_template
import pandas as pd
from joblib import load
from config.db_config import db_connection_pool
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('formulario.html')

# Cargar el modelo entrenado
modelo_entrenado = load('modelo_entrenado.joblib')

# Función para cargar datos desde la base de datos
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

# Codificar one-hot los datos fuera de la función de predicción
datos = cargar_datos_desde_bd()
datos_encoded = pd.get_dummies(datos, columns=['historial_crediticio', 'ingresos_deudas'])

# Obtener las columnas utilizadas durante el entrenamiento
columnas_modelo = datos_encoded.drop(['id', 'nombre', 'apellido', 'cumple_normativas'], axis=1).columns

# Guardar el conjunto de datos codificado y las columnas para su uso posterior
datos_codificados = datos_encoded.drop(['id', 'nombre', 'apellido', 'cumple_normativas'], axis=1)
X_train = datos_codificados.columns  # Asígnalo a X_train para que el nombre sea consistente con el código original

# Función para predecir la probabilidad de aprobación
def predecir_probabilidad_aprobacion(nombre, apellido, X_train=datos_codificados.columns):
    # Cargar los datos de la base de datos
    datos = cargar_datos_desde_bd()
    
    # Filtrar datos para obtener el registro del solicitante
    solicitante = datos[(datos['nombre'] == nombre) & (datos['apellido'] == apellido)]
    
    if solicitante.empty:
        # Si no se encuentra el solicitante en la base de datos
        return None
    
    # Preprocesar los datos del solicitante para hacer la predicción
    solicitante_encoded = pd.get_dummies(solicitante.drop(['id', 'nombre', 'apellido', 'cumple_normativas'], axis=1))
    
    # Asegurarse de que el conjunto de datos de predicción tenga las mismas columnas que el conjunto de entrenamiento
    columnas_faltantes = set(X_train) - set(solicitante_encoded.columns)
    for columna in columnas_faltantes:
        solicitante_encoded[columna] = 0  # Agregar columnas faltantes con valores 0
    
    # Reordenar las columnas para que coincidan con el orden del conjunto de entrenamiento
    solicitante_encoded = solicitante_encoded[X_train]
    
    # Si la solicitud no cumple con los requisitos mínimos para la predicción
    if solicitante_encoded.empty:
        return None
    
    # Hacer la predicción de probabilidad de aprobación
    probabilidad_aprobacion = modelo_entrenado.predict_proba(solicitante_encoded)[:, 1][0]
    
    return probabilidad_aprobacion

# Función para determinar si la solicitud fue aprobada o rechazada
def determinar_aprobacion(probabilidad_aprobacion, umbral=0.5):
    if probabilidad_aprobacion is None:
        return "No se pudo evaluar"  # Si no se puede evaluar, por ejemplo, si falta información
        
    if probabilidad_aprobacion > umbral:
        return "Aprobado"
    else:
        return "Rechazado"

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    historial_crediticio = request.form['historial_crediticio']
    ingresos_deudas = request.form['ingresos_deudas']
    tiempo_empleo_actual = request.form['tiempo_empleo_actual']
    tiempo_residencia_actual = request.form['tiempo_residencia_actual']
    monto_solicitado = float(request.form['monto_solicitado'])  # Asume que monto_solicitado es un campo numérico
    edad = request.form['edad']
    experiencia_crediticia = request.form['experiencia_crediticia']
    cumple_normativas = request.form.get('cumple_normativas')  # Podría ser None si no se selecciona

    # Utilizar el modelo entrenado para predecir la probabilidad de aprobación
    probabilidad_aprobacion = predecir_probabilidad_aprobacion(nombre, apellido)
    
    # Determinar si la solicitud fue aprobada o rechazada
    resultado_evaluacion = determinar_aprobacion(probabilidad_aprobacion)

    return render_template('resultados.html', nombre=nombre, apellido=apellido, monto_solicitado=monto_solicitado, 
                           probabilidad_aprobacion=probabilidad_aprobacion, resultado_evaluacion=resultado_evaluacion)

if __name__ == '__main__':
    app.run(debug=True)