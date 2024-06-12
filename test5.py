import time
from cinema import CinemaDatabase
from datetime import datetime, timedelta 
import random

def generar_fecha_aleatoria():
    hoy = datetime.now()
    # Generar un número aleatorio de días después de hoy
    dias_aleatorios = random.randint(1, 365)
    # Generar un número aleatorio de segundos en el día
    segundos_aleatorios = random.randint(0, 86399)
    # Calcular la fecha y hora aleatoria
    fecha_aleatoria = hoy + timedelta(days=dias_aleatorios, seconds=segundos_aleatorios)
    # Formatear la fecha en el formato "2024-05-27 15:00:00"
    fecha_formateada = fecha_aleatoria.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_formateada

def stress_test_5(cinema_db, reservation_id, movie_name, show_time, test_seat_number, new_test_user_name, iterations):
    start_time = time.time()
    successful_updates = 0

    for _ in range(iterations):
        # Intentar actualizar la reserva
        if cinema_db.update_reservation(reservation_id, movie_name, show_time, test_seat_number, generar_fecha_aleatoria()):
            successful_updates += 1

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total de actualizaciones exitosas: {successful_updates}")
    print(f"Tiempo total tomado: {total_time} segundos")

# Crear una instancia de la base de datos del cine
cinema_db = CinemaDatabase()

# Detalles de la reserva a actualizar
test_movie_name = "TestMovie"
test_show_time = datetime.now()
test_user_name = "Juanjo"
test_seat_number = 5
new_test_user_name = "Work_the_house"

reservation_id = cinema_db.reserve_seat(test_movie_name, test_user_name, test_show_time, test_seat_number)

# Ejecutar el test de estrés
stress_test_5(cinema_db, reservation_id, test_movie_name, test_show_time, test_seat_number, new_test_user_name, iterations=1000)
