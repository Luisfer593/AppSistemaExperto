import pandas as pd
from config.db_config import db_connection_pool
from mysql.connector import Error
from joblib import load

# Función para obtener las reglas y heurísticas desde la base de datos
def obtener_reglas_heuristicas():
    try:
        with db_connection_pool.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT descripcion, tipo, condicion FROM reglas_heuristicas")
                reglas_heuristicas = cursor.fetchall()
                # Convertir el valor de la columna condicion a cadena de texto
                reglas_heuristicas = [{'descripcion': descripcion, 'tipo': tipo, 'condicion': str(condicion)} 
                                      for descripcion, tipo, condicion in reglas_heuristicas]
                return reglas_heuristicas
    except Error as err:
        print(f"Error de MySQL: {err}")
        return []

# Función para obtener el último registro de la tabla solicitudes_credito
def obtener_ultimo_registro():
    try:
        connection = db_connection_pool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM solicitudes_credito ORDER BY id DESC LIMIT 1")
            ultimo_registro = cursor.fetchone()
            return ultimo_registro
    except Error as e:
        print("Error al obtener el último registro:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Función para evaluar reglas y heurísticas
def evaluar_reglas_heuristicas(nombre, apellido):
    reglas_heuristicas = obtener_reglas_heuristicas()
    ultimo_registro = obtener_ultimo_registro()

    resultado_final = None  # Variable para almacenar el resultado
    porcentaje = None

    try:
        if reglas_heuristicas:  # Verificar si hay reglas heurísticas disponibles
            # Crear un DataFrame con los datos del último registro
            df_solicitante = pd.DataFrame(ultimo_registro, index=[0])

            # Definir umbral de aprobación
            umbral_aprobacion = 70

            # Inicializar contador de reglas aprobadas
            reglas_aprobadas = 0

            for regla_heuristica in reglas_heuristicas:
                tipo = regla_heuristica['tipo']  # 'Regla' o 'Heuristica'
                descripcion = regla_heuristica['descripcion']

                # Evaluar cada regla o heurística
                if tipo == 'Regla':
                    condicion = regla_heuristica['condicion']
                    resultado_evaluacion = df_solicitante.query(condicion).shape[0] > 0
                elif tipo == 'Heuristica':
                    # Lógica para heurísticas específicas
                    if descripcion == 'Si el solicitante cumple con todos los requisitos anteriores y tiene una calificación crediticia alta, se aprueba automáticamente.':
                        resultado_evaluacion = df_solicitante['calificacion_crediticia'] == 'Alta'
                    elif descripcion == 'Si hay evidencia de riesgo crediticio significativo en múltiples áreas (historial crediticio, relación ingresos-deudas, estabilidad laboral, etc.), se podría requerir una revisión más detallada o incluso denegar el crédito.':
                        # Lógica para la heurística específica
                        resultado_evaluacion = evaluar_heuristica_riesgo_crediticio(df_solicitante)

                # Contar reglas aprobadas
                if resultado_evaluacion:
                    reglas_aprobadas += 1

            # Calcular porcentaje de aprobación solo si hay reglas heurísticas disponibles
            porcentaje = (reglas_aprobadas / len(reglas_heuristicas)) * 100

            # Determinar resultado final
            if porcentaje >= umbral_aprobacion:
                resultado_final = "Aprobado"
                acciones_aprobacion(df_solicitante)  # Puedes agregar acciones específicas aquí
            else:
                resultado_final = "Rechazado"
                acciones_rechazo(df_solicitante)  # Puedes agregar acciones específicas aquí
        else:
            print("No hay reglas heurísticas disponibles.")
            resultado_final = "Rechazado"  # Si no hay reglas, rechazar solicitud

    except Error as e:
        print("Error al procesar los datos del último registro:", e)

    # Devuelve el resultado final basado en la evaluación de las reglas y heurísticas
    return resultado_final, porcentaje


def evaluar_heuristica_riesgo_crediticio(df_solicitante):
    # Evaluar el riesgo crediticio basándose en los datos del solicitante
    # Por ejemplo, si el historial crediticio es malo y la relación ingresos-deudas no cumple con cierto criterio, considerarlo como alto riesgo
    historial_crediticio = df_solicitante['historial_crediticio']
    ingresos_deudas = df_solicitante['ingresos_deudas']
    
    if historial_crediticio == 'Malo' and ingresos_deudas == 'Alto':
        return True  # Alto riesgo
    else:
        return False  # Riesgo bajo o moderado
    
def acciones_aprobacion(df_solicitante):
    # Acciones a realizar en caso de aprobación
    # Por ejemplo, enviar una notificación al solicitante
    print("La solicitud ha sido aprobada. Acciones adicionales a realizar.")

def acciones_rechazo(df_solicitante):
    # Acciones a realizar en caso de rechazo
    # Por ejemplo, enviar una notificación al solicitante indicando el motivo del rechazo
    print("La solicitud ha sido rechazada. Acciones adicionales a realizar.")

# Función para cargar el modelo entrenado
def cargar_modelo_entrenado():
    try:
        # Cargar el modelo desde el archivo modelo_entrenado.joblib
        modelo = load('modelo_entrenado.joblib')
        return modelo
    except Exception as e:
        print(f"Error al cargar el modelo entrenado: {e}")
        return None

def predecir_probabilidad_aprobacion(nombre, apellido):
    # Lógica para predecir la probabilidad de aprobación basada en el modelo entrenado
    # Por ejemplo, cargar el modelo entrenado y utilizarlo para hacer la predicción
    modelo = cargar_modelo_entrenado()
    if modelo:
        # Realizar la predicción utilizando el modelo cargado
        # Se puede utilizar cualquier lógica específica del modelo
        # Esta es solo una demostración de cómo se podría implementar
        # prediccion = modelo.predict([nombre, apellido])
        # return predicción
        return 0.75  # Solo para fines de demostración

