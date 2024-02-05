# sistema_experto_financiero.py

from config.db_config import db_connection_pool
from mysql.connector import Error
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def pagina_principal():
    return render_template('formulario.html')

# Función para insertar una solicitud en la base de datos
def insertar_solicitud(nombre, apellido, historial_crediticio, ingresos_deudas):
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor() as cursor:
                insert_query = """
                INSERT INTO solicitudes_credito (nombre, apellido, historial_crediticio, ingresos_deudas)
                VALUES (%s, %s, %s, %s)
                """
                datos_solicitante = (nombre, apellido, historial_crediticio, ingresos_deudas)
                cursor.execute(insert_query, datos_solicitante)
                connection.commit()
                print("Solicitud insertada correctamente.")

    except Error as err:
        print(f"Error de MySQL: {err}")

# Función para evaluar estabilidad laboral y residencial
def evaluar_estabilidad_laboral_residencial(nombre, apellido):
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = "SELECT tiempo_empleo_actual, tiempo_residencia_actual FROM solicitudes_credito WHERE nombre = %s AND apellido = %s"
                cursor.execute(query, (nombre, apellido))
                result = cursor.fetchone()

                if result and 'tiempo_empleo_actual' in result and 'tiempo_residencia_actual' in result:
                    if result['tiempo_empleo_actual'] > 3 and result['tiempo_residencia_actual'] > 5:
                        return "Aprobado"
                    else:
                        return "Rechazado"
                else:
                    return "Rechazado"

    except Error as err:
        print(f"Error de MySQL: {err}")
        return "Error en la evaluación"

# Función para evaluar razonabilidad del monto solicitado
def evaluar_razonabilidad_monto(nombre, apellido, monto_solicitado):
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = "SELECT ingresos FROM solicitudes_credito WHERE nombre = %s AND apellido = %s"
                cursor.execute(query, (nombre, apellido))
                result = cursor.fetchone()

                if result and monto_solicitado < 0.5 * result['ingresos']:
                    return "Aprobado"
                else:
                    return "Rechazado"

    except Error as err:
        print(f"Error de MySQL: {err}")
        return "Error en la evaluación"

# Función para evaluar edad y experiencia crediticia
def evaluar_edad_experiencia(nombre, apellido, edad, experiencia_crediticia):
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = "SELECT edad, experiencia_crediticia FROM solicitudes_credito WHERE nombre = %s AND apellido = %s"
                cursor.execute(query, (nombre, apellido))
                result = cursor.fetchone()

                if result and result['edad'] > 25 and result['experiencia_crediticia'] > 2:
                    return "Aprobado"
                else:
                    return "Rechazado"

    except Error as err:
        print(f"Error de MySQL: {err}")
        return "Error en la evaluación"

# Función para evaluar cumplimiento de normativas
def evaluar_cumplimiento_normativas(nombre, apellido):
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = "SELECT cumple_normativas FROM solicitudes_credito WHERE nombre = %s AND apellido = %s"
                cursor.execute(query, (nombre, apellido))
                result = cursor.fetchone()

                if result and result['cumple_normativas']:
                    return "Aprobado"
                else:
                    return "Rechazado"

    except Error as err:
        print(f"Error de MySQL: {err}")
        return "Error en la evaluación"

# Ruta para procesar el formulario
# Ruta para procesar el formulario
@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    historial_crediticio = request.form['historial_crediticio']
    ingresos_deudas = request.form['ingresos_deudas']
    monto_solicitado = float(request.form['monto_solicitado'])  # Asume que monto_solicitado es un campo numérico

    insertar_solicitud(nombre, apellido, historial_crediticio, ingresos_deudas)

    # Evaluar reglas y heurísticas
    resultado_estabilidad = evaluar_estabilidad_laboral_residencial(nombre, apellido)
    resultado_razonabilidad = evaluar_razonabilidad_monto(nombre, apellido, monto_solicitado)
    # Continuar con las demás funciones de evaluación...

    return render_template('resultados.html', resultado_estabilidad=resultado_estabilidad, resultado_razonabilidad=resultado_razonabilidad)

if __name__ == '__main__':
    app.run(debug=True)
