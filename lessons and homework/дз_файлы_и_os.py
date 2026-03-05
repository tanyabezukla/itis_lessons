import os


# Функции
# add_note(title, text) - Создаёт файл notes/title.txt и записывает туда текст.
# list_notes() - Выводит список всех файлов в папке.
# read_note(title) - Выводит содержимое файла.
# delete_note(title) - Удаляет файл.
# clear_notes() - Удаляет все заметки.
# Что нужно учесть:
# Программа не должна падать, поэтому необходимо сделать обработку ошибок или написать соответствующие условия, чтобы программа не падала.
# Необходимо написать класс NotesManager, который будет содержать в себе все нужные методы.
# Помимо известных нам способов решения задач выше, программа также подразумевает использование функций из библиотеки os, которые мы не рассматривали на паре - ваша задача подобрать необходимые.
# Нужно добавить меню действий, чтобы пользователь работал с менеджером заметок, пока сам не остановил программу.


NOTES_DIR = os.path.join('notes')


if not os.path.exists(NOTES_DIR):
    os.mkdir(NOTES_DIR)


class NotesManager:
    def add_note(self, title, text):
        file_path = os.path.join(NOTES_DIR, f'{title}.txt')
        try:
            if os.path.exists(file_path):
                raise FileExistsError(f'The note {title} already exist')

            with open(file_path,'w') as f:
                f.write(text)

            print('The note has been written')

        except FileExistsError as e:
            print(e)

    def list_notes(self):
        try:
            notes = os.listdir(NOTES_DIR)
            if not notes:
                raise FileNotFoundError('there is no notes')

            print('List of notes')
            for note in notes:
                print(f'\n {note}')

        except FileNotFoundError as e:
            print(e)

    def read_note(self, title):
        file_path = os.path.join(NOTES_DIR, f'{title}.txt')
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f'The note {title} wasnt found')

            with open(file_path, 'r') as f:
                content = f.read()

            print(f'{title}')
            print(f'\n {content}')

        except FileNotFoundError as e:
            print(e)

    def delete_note(self, title):
        file_path = os.path.join(NOTES_DIR, f'{title}.txt')
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f'The note {title} wasnt found')

            os.remove(file_path)
            print(f'the note {title} was deleted')

        except FileNotFoundError as e:
            print(e)



    def clear_notes(self):
        try:
            notes = os.listdir(NOTES_DIR)
            if not notes:
                raise FileNotFoundError('notes wasnt found')

            for note in notes:
                os.remove(os.path.join(NOTES_DIR, note))

            print('Notes was deleted')
        except FileNotFoundError as e:
            print(e)

manager = NotesManager()

while True:
    print('\n менеджер заметок')
    print('1 - добавить заметку')
    print('2 - список заметок')
    print('3 - читать заметку')
    print('4 - удалить заметку')
    print('5 - удалить все заметки')
    print('0 - выйти')

    choice = input('выбери действие: ')

    if choice == '1':
        title = input('название заметки: ')
        text = input('текст заметки: ')
        manager.add_note(title, text)
    elif choice == '2':
        manager.list_notes()
    elif choice == '3':
        title = input('название заметки: ')
        manager.read_note(title)
    elif choice == '4':
        title = input('название заметки: ')
        manager.delete_note(title)
    elif choice == '5':
        manager.clear_notes()
    elif choice == '0':
        print('выход из программы')
        break
    else:
        print('неверный ввод, попробуй снова')
