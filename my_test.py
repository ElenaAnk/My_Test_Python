import json
import random
import re
from datetime import datetime
from pprint import pprint

def first_start():
    global data, outfile
    data = dict()
    data["notebook"] = []
    with open('notebook_new.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
#first_start()

def new_data():
    global f, data, outfile
    note_new = dict()
    note_new["id"] = random.randint(0, 1000)
    note_new["title"] = input("Введите заголовок заметки: ")
    note_new["note"] = input("Введите заметку: ")
    note_new["date"] = datetime.now().isoformat(timespec='minutes')
    with open('notebook_new.json', encoding='utf8') as f:
        data = json.load(f)
    data['notebook'].append(note_new)
    with open('notebook_new.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
new_data()
def print_alls_note():
    global f, text
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        text = json.load(f)
        pprint(text)
print_alls_note()
def id_search():
    global f, data
    search_id = int(input("Введите id заметки,который необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        for txt in data["notebook"]:
            if txt["id"] == search_id:
                print(data["notebook"][minimal])
            else:
                None
            minimal = minimal + 1

#id_search()

def title_search():
    global f, data
    search_title = str(input("Введите заголовок заметки, который необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        for txt in data["notebook"]:
            if txt["title"] == search_title:
                print(data["notebook"][minimal])
            else:
                None
            minimal = minimal + 1

#title_search()

def note_search():
    global f, data
    search_note = str(input("Введите часть текста заметки, которую необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        for txt in data["notebook"]:
            if re.search(search_note, txt["note"]):
                print(data["notebook"][minimal])
            else:
                None
            minimal = minimal + 1

#note_search()

def date_search():
    global f, data
    search_date = str(input("Введите дату заметки, которую необходимо найти: "))
    with open("notebook_new.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        minimal = 0
        for txt in data["notebook"]:
            if re.search(search_date, txt["date"]):
                print(data["notebook"][minimal])
            else:
                None
            minimal = minimal + 1

#date_search()

def delete_note():
    global f, data, outfile
    note_del = int(input("Введите id заметки, которую хотите удалить: "))
    with open('notebook_new.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        for txt in data['notebook']:
            if txt['id'] == note_del:
                data['notebook'].pop(minimal)
            else:
                None
            minimal = minimal + 1
        with open('notebook_new.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

#delete_note()

def edit_note():
    global f, data, outfile
    note_edit = int(input("Введите id заметки, которую хотите отредактировать: "))
    with open('notebook_new.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        for txt in data['notebook']:
            if txt['id'] == note_edit:
                txt["title"] = input("Введите заголовок заметки: ")
                txt["note"] = input("Введите заметку: ")
                txt["date"] = datetime.now().isoformat(timespec='minutes')
            else:
                None
            minimal = minimal + 1
        with open('notebook_new.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

#edit_note()