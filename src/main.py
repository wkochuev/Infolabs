from database.db import create_tables, insert_sample_data
from repository.repository import Repository
import os

DB_FILE = "arendas.db"

def main():
    role="Guest"
    # Если базы нет, создаем таблицы и вставляем тестовые данные
    if not os.path.exists(DB_FILE):
        create_tables(DB_FILE)
        insert_sample_data(DB_FILE)

    repo = Repository(DB_FILE)

    # --- Основной цикл программы ---
    while True:
        print("\nВыберите действие:")
        print("1 - Показать все объявления")
        print("2 - Экспорт таблицы Арендодателей в 4 разных файла")
        if role=="Arendat":
            print("3 - Откликнуться на заявку")
        if role=="Arendodat":
            print("3 - Создать объявление")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            rents = repo.get_all_rents()

            print("\nСписок всех объявлений:")
            for renta in rents:
                room = repo.get_room(renta.room_id)
                arendodat = repo.get_arendodat(room.arendodat_id)
                resp= repo.get_response(renta.id)
                arendat=repo.get_arendat(resp.arendat_id)
                print(f"{renta.id}: {renta.content} [Стоимость: {renta.cost}] [Адрес: {room.adress}] (Автор объявления: {arendodat.name}, Отозвался: {arendat.name})")

        elif choice=="2":
            repo.save_data()

        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    repo.close()

if __name__ == "__main__":
    main()