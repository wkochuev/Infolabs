import sqlite3;
 
arendas_db = sqlite3.connect("arendas.db")
cursor = arendas_db.cursor()
 
# создаем таблицу people
cursor.execute("""CREATE TABLE arendators
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                username TEXT)
            """)
