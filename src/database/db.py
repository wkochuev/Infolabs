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
        CREATE TABLE IF NOT EXISTS Rent (
            ID INTEGER PRIMARY KEY,
            Content TEXT NOT NULL,
            Arendodat_ID INTEGER,
            Arendat_ID INTEGER,
            FOREIGN KEY (Arendodat_ID) REFERENCES Arendodat(ID)
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

    # Проверка, есть ли объявления
    cursor.execute("SELECT COUNT(*) FROM Rent")
    if cursor.fetchone()[0] == 0:
        rent = [
            ("Сдаю комнату в Сормово", 2, 1),
            ("Сдаю корабль с беззащитными членами экипажа.",5, 2),
            ("Сдаю пиццерию на ночное время, охрана не помешает!",3, 5)
        ]
        cursor.executemany("INSERT INTO Rent (Content, Arendodat_ID, Arendat_ID) VALUES (?, ?, ?)", rent)
        print("Добавлены объявления.")


    conn.commit()
    conn.close()