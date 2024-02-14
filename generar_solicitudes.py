import random
from faker import Faker
from mysql.connector import Error

# Importar la conexión a la base de datos
from config.db_config import db_connection_pool

# Configurar Faker para generar datos en español
fake = Faker('es_ES')

# Generar datos ficticios para solicitudes de crédito
def generar_solicitudes_credito(cantidad):
    solicitudes = []

    for _ in range(cantidad):
        monto_solicitado = round(random.uniform(1, 50)) * 1000  # Generar valores exactos en miles
        solicitud = {
            'nombre': f"{fake.first_name()} {fake.first_name()}",
            'apellido': f"{fake.last_name()} {fake.last_name()}",
            'historial_crediticio': random.choice(['Bueno', 'Regular', 'Malo']),
            'ingresos_deudas': random.choice(['Cumple', 'No Cumple']),
            'tiempo_empleo_actual': random.randint(1, 10),
            'tiempo_residencia_actual': random.randint(1, 10), 
            'monto_solicitado': monto_solicitado,
            'edad': random.randint(18, 75),
            'experiencia_crediticia': random.randint(1, 10),
            'cumple_normativas': random.choice([1, 0])
        }
        solicitudes.append(solicitud)

    return solicitudes

def insertar_solicitud_en_db(solicitud):
    try:
        # Obtener una conexión de la piscina
        connection = db_connection_pool.get_connection()

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Preparar la consulta SQL para la inserción
   # Preparar la consulta SQL para la inserción
        insert_query = "INSERT INTO solicitudes_credito (nombre, apellido, historial_crediticio, ingresos_deudas, tiempo_empleo_actual, tiempo_residencia_actual, monto_solicitado, edad, experiencia_crediticia, cumple_normativas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Obtener los valores de la solicitud
        values = (
            solicitud['nombre'],
            solicitud['apellido'],
            solicitud['historial_crediticio'],
            solicitud['ingresos_deudas'],
            solicitud['tiempo_empleo_actual'],
            solicitud['tiempo_residencia_actual'],
            solicitud['monto_solicitado'],
            solicitud['edad'],
            solicitud['experiencia_crediticia'],
            solicitud['cumple_normativas']
        )

        # Ejecutar la consulta
        cursor.execute(insert_query, values)

        # Hacer commit para confirmar la inserción
        connection.commit()

    except Error as e:
        print("Error al insertar en la base de datos:", e)

    finally:
        # Asegurarse de cerrar el cursor y la conexión, incluso si hay un error
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    cantidad_solicitudes = 100
    solicitudes_generadas = generar_solicitudes_credito(cantidad_solicitudes)


    for solicitud in solicitudes_generadas:
        insertar_solicitud_en_db(solicitud)
        print(solicitud)

