from cinema import CinemaDatabase
import threading

# Función para realizar muchas reservas rápidamente
def stress_test_1(client_id, num_requests):
    db = CinemaDatabase()

    for _ in range(num_requests):
        db.reserve_seat("Avengers", f"User{client_id}", "2024-05-27 15:00:00", 5)

    del db

# Ejecutar el stress test con un solo cliente
stress_test_1(1, 10000)