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

class Rent:
    """
    Модель для таблицы Rent
    Поля:
    - id: уникальный идентификатор книги (PK)
    - content: текст объявления
    - arendodat_id: идентификатор арендодателя (FK -> Aarendodat.id)
    - arendat_id: идентификатор арендатора (FK -> Aarendat.id)
    """
    def __init__(self, id, content, arendodat_id, arendat_id ):
        self.id = id
        self.content = content
        self.arendodat_id = arendodat_id
        self.arendat_id = arendat_id