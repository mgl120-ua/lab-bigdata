import threading
from cinema import CinemaDatabase

condition = threading.Condition()
turn = "Client1"

def reserve_seats(cinema_db, client_name):
    global turn
    for seat_number in range(1, 101):
        with condition:
            # Esperar hasta que sea el turno de este cliente
            while turn != client_name:
                condition.wait()
            
            # Realizar la reserva
            print(f"{client_name} reservando asiento {seat_number}")  # Agregar print para depuración
            if cinema_db.reserve_seat("Avengers", client_name, "2024-05-27 15:00:00", seat_number):
                 turn = "Client2" if turn == "Client1" else "Client1"
            else:
                 turn = "Client1" if turn == "Client1" else "Client2"
            
            # Notificar al otro hilo que puede continuar
            condition.notify_all()

if __name__ == "__main__":
    cinema_db = CinemaDatabase()

    # Crear hilos para realizar el proceso de ocupación de asientos
    clients = ["Client1", "Client2"]
    threads = []
    for client in clients:
        t = threading.Thread(target=reserve_seats, args=(cinema_db, client))
        threads.append(t)
        t.start()

    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()

    print("Todos los asientos han sido ocupados.")