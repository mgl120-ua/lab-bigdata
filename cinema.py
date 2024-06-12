from cassandra.cluster import Cluster
from datetime import datetime
import uuid


class CinemaDatabase:
    def __init__(self, contact_points=['cas1', 'cas2', 'cas3'], keyspace='cinema'):
        self.cluster = Cluster(contact_points)
        self.session = self.cluster.connect(keyspace)

    def __del__(self):
        self.session.shutdown()
        self.cluster.shutdown()

    def reserve_seat(self, movie_name, user_name, show_time, seat_number):
        # Verificar si el asiento está disponible en el momento dado
        reservation = self.session.execute(
            "SELECT * FROM Reservations WHERE movie_name=%s AND show_time=%s AND seat_number=%s ALLOW FILTERING",
            (movie_name, show_time, seat_number)
        ).one()
        if reservation:
            print("El asiento ya está reservado para esa película y hora.")
            return False
        
        # Verificar si el asiento existe
        if seat_number > 100:
            print("El asiento no existe para esa película.")
            return False
        
        # Realizar la reserva
        reservation_id = uuid.uuid4()
        created_at = datetime.now()
        self.session.execute(
            "INSERT INTO Reservations (reservation_id, movie_name, user_name, show_time, seat_number, created_at) VALUES (%s, %s, %s, %s, %s, %s)",
            (reservation_id, movie_name, user_name, show_time, seat_number, created_at)
        )
        print(f"Reserva exitosa. ID de reserva: {reservation_id}")
        return reservation_id


    def view_reservation_by_id(self, reservation_id):
        # Verificar si la reserva existe
        reservation = self.session.execute("SELECT * FROM Reservations WHERE reservation_id=%s ALLOW FILTERING", (reservation_id,)).one()
        if not reservation:
            print("La reserva especificada no existe.")
            return None
        
        print(f"ID de Reserva: {reservation.reservation_id}")
        print(f"Película: {reservation.movie_name}")
        print(f"Usuario: {reservation.user_name}")
        print(f"Hora de la función: {reservation.show_time}")
        print(f"Número de Asiento: {reservation.seat_number}")
        return reservation

    def view_reservation(self, movie_name, show_time, seat_number):
        reservation = self.session.execute(
            """
            SELECT * FROM Reservations WHERE movie_name=%s AND show_time=%s AND seat_number=%s ALLOW FILTERING
            """,
            (movie_name, show_time, seat_number)
        ).one()
        if reservation:
            print(f"ID de Reserva: {reservation.reservation_id}")
            print(f"Película: {reservation.movie_name}")
            print(f"Usuario: {reservation.user_name}")
            print(f"Hora de la función: {reservation.show_time}")
            print(f"Número de Asiento: {reservation.seat_number}")
            return reservation
        else:
            print("No se encontró ninguna reserva para la película, hora y asiento especificados.")


    def update_reservation(self, reservation_id, movie_name, show_time, seat_number, new_show_time):
        update_query = "UPDATE Reservations SET show_time=%s WHERE reservation_id=%s"
        update_params = (new_show_time, reservation_id)
        if not self.view_reservation_by_id(reservation_id):
            print(">Error")
            return False
        else:
            self.session.execute(update_query, update_params)
            print("Reserva actualizada exitosamente.")
            return False

    def cancel_reservation_by_id(self, reservation_id):
        # Verificar si la reserva existe
        if not self.session.execute("SELECT * FROM Reservations WHERE reservation_id=%s ALLOW FILTERING", (reservation_id,)).one():
            print("La reserva especificada no existe.")
            return False
        
        # Cancelar la reserva
        self.session.execute("DELETE FROM Reservations WHERE reservation_id=%s", (reservation_id,))
        print("Reserva cancelada exitosamente.")
        return True

    def cancel_reservation(self, movie_name, show_time, seat_number):
        # Verificar si la reserva existe
        reservation = self.view_reservation(movie_name, show_time, seat_number)
        if not reservation:
            print("La reserva especificada no existe.")
            return False
        
        # Cancelar la reserva
        self.session.execute("DELETE FROM Reservations WHERE reservation_id=%s", (reservation.reservation_id,))
        print("Reserva cancelada exitosamente.")
        return True