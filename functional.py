import random
import re
from datetime import datetime
import json
from pprint import pprint


def first_start(): #первый запуск для работы с заметками (создает пустую json для будущего заполнения)
    global data, outfile
    notebook = []
    with open('notebook_new.json', 'w', encoding='utf8') as outfile:
        json.dump(notebook, outfile, ensure_ascii=False, indent=2)

def new_data(): #добавление записей в блокнот
    global f, data, outfile
    note_new = dict()
    note_new["id"] = random.randint(0, 1000)
    note_new["title"] = input("Введите заголовок заметки: ")
    note_new["note"] = input("Введите заметку: ")
    note_new["date"] = datetime.now().isoformat(timespec='minutes')
    with open('notebook_new.json', encoding='utf8') as f:
        data = json.load(f)
    data.append(note_new)
    with open('notebook_new.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
    print("Заметка создана успешно")


def print_alls_note(): #показывает все заметки на экране
    global f, text
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        text = json.load(f)
        pprint(text)


def id_search(): #поиск заметки по id
    global f, data
    search_id = int(input("Введите id заметки,которую необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if txt["id"] == search_id:
                print(data[minimal])
                flag = False
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данный id не найден")    

def title_search(): #поиск заметки по заголовку
    global f, data
    search_title = str(input("Введите заголовок заметки, который необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if txt["title"] == search_title:
                print(data[minimal])
                flag = False
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данный заголовок не найден")    

def note_search(): #поиск заметки по отрывку в тексте
    global f, data
    search_note = str(input("Введите часть текста заметки, которую необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if re.search(search_note, txt["note"]):
                print(data[minimal])
                flag = False
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данный текст не найден")     

def date_search(): #поиск заметки по дате 
    global f, data
    search_date = str(input("Введите дату в формате: yyyy-mm-dd: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if re.search(search_date, txt["date"]):
                print(data[minimal])
                flag = False
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данная дата не найдена")     

def delete_note(): #удаление заметки по id
    global f, data, outfile
    note_del = int(input("Введите id заметки, которую хотите удалить: "))
    with open('notebook_new.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if txt['id'] == note_del:
                data.pop(minimal)
                flag = False
                print("Заметка успешно удалена")
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данный id не найден")    
        with open('notebook_new.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
             

def edit_note(): #редактирование заметки по id
    global f, data, outfile
    note_edit = int(input("Введите id заметки, которую хотите отредактировать: "))
    with open('notebook_new.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        flag = True
        for txt in data:
            if txt['id'] == note_edit:
                txt["title"] = input("Введите заголовок заметки: ")
                txt["note"] = input("Введите заметку: ")
                txt["date"] = datetime.now().isoformat(timespec='minutes')
                flag = False
            else:
                None
            minimal = minimal + 1
        if flag:
            print("Данный id не найден")     
        with open('notebook_new.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

