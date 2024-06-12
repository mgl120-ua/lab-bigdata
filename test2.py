import random
import string
import threading
import time
from datetime import datetime
from cinema import CinemaDatabase

def random_string(length):
    """Genera una cadena aleatoria de longitud dada."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def make_random_reservation(cinema_db):
    """Realiza una reserva aleatoria."""
    movie_name = random_string(8)
    user_name = random_string(6)
    show_time = datetime.now()
    seat_number = random.randint(1, 100)
    cinema_db.reserve_seat(movie_name, user_name, show_time, seat_number)

def stress_test_2(cinema_db, num_requests):
    """Dos o más clientes realizan solicitudes aleatorias."""
    threads = []
    for _ in range(num_requests):
        t = threading.Thread(target=make_random_reservation, args=(cinema_db,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


cinema_db = CinemaDatabase()

start_time = time.time()
stress_test_2(cinema_db, 10000)
end_time = time.time()

print(f"Stress Test 2 completado en {end_time - start_time} segundos.")
