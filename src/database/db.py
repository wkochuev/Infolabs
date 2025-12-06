import sqlite3
from sqlite3 import Connection

def get_connection(db_name: str = "arendas.db") -> Connection:
    return sqlite3.connect(db_name)


def create_tables(db_name: str = "arendas.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Arendat (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Arendodat (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Room (
            ID INTEGER PRIMARY KEY,
            Adress TEXT NOT NULL,
            Arendodat_ID INTEGER,
            FOREIGN KEY (Arendodat_ID) REFERENCES Arendodat(ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rent (
            ID INTEGER PRIMARY KEY,
            Content TEXT NOT NULL,
            Cost INTEGER,
            Room_ID INTEGER,
            FOREIGN KEY (Room_ID) REFERENCES Room(ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Response (
            ID INTEGER PRIMARY KEY,
            Arendat_ID INTEGER,
            Rent_ID INTEGER,
            FOREIGN KEY (Rent_ID) REFERENCES Rent(ID),
            FOREIGN KEY (Arendat_ID) REFERENCES Arendat(ID)
        )
    ''')


    conn.commit()
    conn.close()


def insert_sample_data(db_name: str = "arendas.db"):
    conn = get_connection(db_name)
    cursor = conn.cursor()

    # Проверка, есть ли арендодатели
    cursor.execute("SELECT COUNT(*) FROM Arendodat")
    if cursor.fetchone()[0] == 0:
        arendodat = [
            ("Max",),
            ("Polinchik",),
            ("Freddy Fazbear",),
            ("Vadim",),
            ("Amogus",)
        ]
        cursor.executemany("INSERT INTO Arendodat (Name) VALUES (?)", arendodat)
        print("Добавлены арендодатели.")

    # Проверка, есть ли арендаторы
    cursor.execute("SELECT COUNT(*) FROM Arendat")
    if cursor.fetchone()[0] == 0:
        arendat = [
            ("Max",),
            ("Imposter",),
            ("Freddy Fazbear",),
            ("Spy",),
            ("Anonimous",)
        ]
        cursor.executemany("INSERT INTO Arendat (Name) VALUES (?)", arendat)
        print("Добавлены арендаторы.")


    # Проверка, есть ли комнаты
    cursor.execute("SELECT COUNT(*) FROM Room")
    if cursor.fetchone()[0] == 0:
        adress = [
            ("ул.Шредингера, д.020", 1),
            ("Штат Оригами", 3),
            ("Космос", 5)
        ]
        cursor.executemany("INSERT INTO Room (Adress, Arendodat_ID) VALUES (?, ?)", adress)
        print("Добавлены комнаты.")

    # Проверка, есть ли объявления
    cursor.execute("SELECT COUNT(*) FROM Rent")
    if cursor.fetchone()[0] == 0:
        rent = [
            ("Сдаю комнату в Сормово", 9999, 1),
            ("Сдаю корабль с беззащитными членами экипажа.", 666, 3),
            ("Сдаю пиццерию на ночное время, охрана не помешает!", 5000, 2)
        ]
        cursor.executemany("INSERT INTO Rent (Content, Cost, Room_ID) VALUES (?, ?, ?)", rent)
        print("Добавлены объявления.")

    # Проверка, есть ли ответы на заявки
    cursor.execute("SELECT COUNT(*) FROM Response")
    if cursor.fetchone()[0] == 0:
        response = [
            (1, 1),
            (2, 2),
            (5, 3)
        ]
        cursor.executemany("INSERT INTO Response (Arendat_ID, Rent_ID) VALUES (?, ?)", response)
        print("Добавлены ответы на заявки.")


    conn.commit()
    conn.close()