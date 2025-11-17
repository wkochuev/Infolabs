import sqlite3

from models.models import Arendodat, Arendat, Rent


class Repository:
    def __init__(self, db_file: str = "arendas.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row  # Позволяет обращаться к колонкам по имени
        self.cursor = self.conn.cursor()

    def get_arendat(self, arendat_id: int):
        self.cursor.execute("SELECT ID, Name FROM Arendat WHERE ID = ?", (arendat_id,))
        row = self.cursor.fetchone()
        if row:
            return Arendat(id=row["ID"], name=row["Name"])
        return None
    
    def get_arendodat(self, arendodat_id: int):
        self.cursor.execute("SELECT ID, Name FROM Arendodat WHERE ID = ?", (arendodat_id,))
        row = self.cursor.fetchone()
        if row:
            return Arendodat(id=row["ID"], name=row["Name"])
        return None
    
    def get_all_rents(self):
        self.cursor.execute("SELECT ID, Content, Arendodat_ID, Arendat_ID FROM Rent")
        rows = self.cursor.fetchall()
        return [Rent(id=row["ID"], content=row["Content"], arendodat_id=row["Arendodat_ID"], arendat_id=row["Arendat_ID"]) for row in rows]

    def reg_arendodat(self, name:str):
        self.cursor.execute("INSERT INTO Arendodat (Name) VALUES (?)", (name))
        #row = self.cursor.fetchone() - вывод последней записи(на будущее)
        self.conn.commit()  
        print("Данные добавлены")
        return None
    
    def reg_arendat(self, name:str):
        self.cursor.execute("INSERT INTO Arendat (Name) VALUES (?)", (name,))
        self.conn.commit()  
        print("Данные добавлены")
        return None

    '''def authoris(self, name: str):
        query = """
            SELECT Arendat.ID, Arendat.Name
            FROM Authors
            JOIN Books ON Authors.ID = Books.Author_ID
            GROUP BY Authors.ID
            HAVING COUNT(Books.ID) > ?
        """
        self.cursor.execute(query, (name,))
        rows = self.cursor.fetchall()
        return [Author(id=row["ID"], name=row["Name"]) for row in rows]'''

    def close(self):
        self.conn.close()