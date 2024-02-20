import json
import os
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, body):
    notes = load_notes()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с таким идентификатором не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с таким идентификатором не найдена.")

def list_notes():
    notes = load_notes()
    if notes:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время: {note['timestamp']}")
    else:
        print("Заметок нет.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            edit_note(note_id, title, body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()