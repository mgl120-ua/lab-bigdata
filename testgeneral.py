from cinema import CinemaDatabase
from datetime import datetime

def test_cinema_database():
    # Crear una instancia de la clase CinemaDatabase
    cinema_db = CinemaDatabase()
    datetimee = datetime.now()

    # Realizar una reserva
    cinema_db.reserve_seat("Avengers", "Usuario1", datetimee, 5)

    # Ver la reserva por ID
    reservation_id = cinema_db.view_reservation("Avengers", datetimee, 5).reservation_id

    # Ver la reserva por nombre de película, hora y número de asiento
    cinema_db.view_reservation("Avengers", datetimee, 5)

    # Actualizar la reserva
    cinema_db.update_reservation(reservation_id, "Usuario1", datetimee, 5, "2024-06-7 15:00:00")

    # Verificar la reserva actualizada
    cinema_db.view_reservation_by_id(reservation_id)

    # Cancelar la reserva por ID
    cinema_db.cancel_reservation_by_id(reservation_id)

    del cinema_db  # Liberar recursos

# Ejecutar la función de prueba
test_cinema_database()
