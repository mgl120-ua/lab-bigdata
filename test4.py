import time
from cinema import CinemaDatabase

def stress_test_4(database, movie_name, show_time, seat_number, iterations):
    start_time = time.time()
    successful_reservations = 0
    successful_cancellations = 0

    for _ in range(iterations):
        # Intentar reservar el asiento
        if database.reserve_seat(movie_name, "TestUser", show_time, seat_number):
            successful_reservations += 1

        # Cancelar la reserva
        if database.cancel_reservation(movie_name, show_time, seat_number):
            successful_cancellations += 1

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total de reservas exitosas: {successful_reservations}")
    print(f"Total de cancelaciones exitosas: {successful_cancellations}")
    print(f"Tiempo total tomado: {total_time} segundos")

# Crear una instancia de la base de datos del cine
cinema_db = CinemaDatabase()

# Detalles del asiento a probar
test_movie_name = "TestMovie"
test_show_time = "2024-05-25 15:00:00"
test_seat_number = 1

# Ejecutar el test de estrés
stress_test_4(cinema_db, test_movie_name, test_show_time, test_seat_number, iterations=10000)
