from functional import new_data
from functional import first_start
from functional import print_alls_note
from functional import id_search
from functional import title_search
from functional import note_search
from functional import date_search
from functional import delete_note
from functional import edit_note


def view_note(): #выбор действия для просмотра заметок
    global command
    command = 0
    while command != "6":
        print("""выберите дейсвите для продолжения:
                            1 - Просмотр всех заметок
                            2 - Просмотр заметки(поиск по id)
                            3 - Просмотр заметки(поиск по дате)
                            4 - Просмотр заметки(поиск по заголовку)
                            5 - Просмотр заметки(поиск по фрагменту текста заметки)
                            6 - Вернуться в предыдущее меню""")
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Введите корректный номер операции")
            command = input("Введите номер операции: ")
        if command == "1":
            print_alls_note()
        elif command == "2":
            id_search()
        elif command == "3":
            date_search()
        elif command == "4":
            title_search()
        elif command == "5":
            note_search()

def continue_work(): #выбор дейсвия для продолжения работы с приложением
    global command
    command = "0"
    while command != "5":
        print("""выберите действите для продолжения:
                        1 - Создание новой заметки
                        2 - Поиск и просмотр заметки
                        3 - Редактирование заметки (поиск по id)
                        4 - Удаление заметки (поиск по id)
                        5 - Вернуться в предыдущее меню""")
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5"):
            print("Введите корректный номер операции")
            command = input("Введите номер операции: ")
        if command == "1":
                new_data()
        elif command == "2":
                view_note()
        elif command == "3":
                edit_note()
        elif command == "4":
                delete_note()

def welcome(): #главный интерфейс 
    global command
    print("Добро пожаловать в приложение ЗАМЕТКИ")
    command = "0"
    while command != "3":
        print("""выберите дейсвите для продолжения:
            1 - Создать приложение заново(очистить все старые записи)
            2 - Продолжить работу в приложении
            3 - Выход""")
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3"):
           print("Введите корректный номер операции")
           command = input("Введите номер операции: ")
        if command == "1":
           first_start()
           print("Приложение очищено, теперь можно добавить первую заметку")
           new_data()
        elif command == "2":
           continue_work()




