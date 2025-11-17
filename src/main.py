from database.db import create_tables, insert_sample_data
from repository.repository import Repository
import os

DB_FILE = "arendas.db"

def main():
    # Если базы нет, создаем таблицы и вставляем тестовые данные
    if not os.path.exists(DB_FILE):
        create_tables(DB_FILE)
        insert_sample_data(DB_FILE)

    repo = Repository(DB_FILE)

    # --- Основной цикл программы ---
    while True:
        print("\nВыберите действие:")
        print("1 - Показать все объявления")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            rents = repo.get_all_rents()
            print("\nСписок всех объявлений:")
            for renta in rents:
                arendodat = repo.get_arendodat(renta.arendodat_id)
                arendat = repo.get_arendat(renta.arendat_id)
                print(f"{renta.id}: {renta.content} (Автор объявления: {arendodat.name}, Отозвался: {arendat.name})")

        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    repo.close()

if __name__ == "__main__":
    main()