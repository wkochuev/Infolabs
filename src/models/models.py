# models/models.py

class Arendodat:
    """
    Модель для таблицы Arendodat
    Поля:
    - id: уникальный идентификатор автора (PK)
    - name: имя арендодателя
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Arendat:
    """
    Модель для таблицы Arendat
    Поля:
    - id: уникальный идентификатор автора (PK)
    - name: имя арендатора
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Room:
    """
    Модель для таблицы Room
    Поля:
    - id: уникальный идентификатор комнаты (PK)
    - adress: текст адреса
    - arendodat_id: идентификатор арендодателя (FK -> Arendodat.id)
    """
    def __init__(self, id, adress, arendodat_id):
        self.id = id
        self.adress = adress
        self.arendodat_id = arendodat_id

class Rent:
    """
    Модель для таблицы Rent
    Поля:
    - id: уникальный идентификатор книги (PK)
    - content: текст объявления
    - cost: целая цена
    - room_id: идентификатор комнаты (FK -> Room.id)
    """
    def __init__(self, id, content, cost, room_id):
        self.id = id
        self.content = content
        self.cost = cost
        self.room_id = room_id

class Response:
    """
    Модель для таблицы Response
    Поля:
    - id: уникальный идентификатор книги (PK)
    - content: текст объявления
    - rent_id: идентификатор объявления (FK -> Rent.id)
    - arendat_id: идентификатор арендатора (FK -> Arendat.id)
    """
    def __init__(self, id, arendat_id, rent_id ):
        self.id = id
        self.arendat_id = arendat_id
        self.rent_id = rent_id