from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import uuid
from datetime import datetime

cluster = Cluster(['cas1', 'cas2', 'cas3'], port=9042)
session = cluster.connect('cinema')

session.execute("DROP TABLE IF EXISTS Reservations", timeout=None)

session.execute("""
CREATE TABLE IF NOT EXISTS Reservations (
    movie_name TEXT,
    show_time TIMESTAMP,
    seat_number INT,
    reservation_id UUID,
    user_name TEXT,
    created_at TIMESTAMP,
    PRIMARY KEY (reservation_id)
)
""")

session.execute("""
CREATE INDEX IF NOT EXISTS idx_movie_name ON Reservations (movie_name)
""")

session.execute("""
CREATE INDEX IF NOT EXISTS idx_show_time ON Reservations (show_time)
""")

session.execute("""
CREATE INDEX IF NOT EXISTS idx_seat_number ON Reservations (seat_number)
""")



# Insertar datos
insert_query = SimpleStatement("""
INSERT INTO Reservations (reservation_id, movie_name, user_name, show_time, seat_number, created_at)
VALUES (%s, %s, %s, %s, %s, %s)
""")
reservation_id = uuid.uuid4()
session.execute(insert_query, (reservation_id, "Avengers", "John Doe", datetime.now(), 5, datetime.now()))

print("Data inserted successfully.")

# Consultar datos
select_query = "SELECT * FROM Reservations"
rows = session.execute(select_query)
for row in rows:
    print(row)