import csv
import os


students = {}

        
def add_student():
    try:
        name = input('Введите имя студента: ').strip()
        if not name:
            print('Имя не может быть пустым')
            return
        
        if name in students:
            print('Студент с этим именем уже существует')
            return

        age = int(input('Введите возраст студента: '))
        if age <= 0 or age > 100:
            print('Возраст должен быть от 0 до 100')
            return

        print('Введите оценки студента через пробел')

        grades_input= input().strip()
        if grades_input:
            grades = list(map(int, grades_input.split()))
            for grade in grades:
                if grade > 5 or grade < 2:
                    print('Оценки должны быть от 2 до 5')
                    return
        else:
            grades = []

        students[name] = {'age': age, 'grades': grades}
        print(f'Студент {name} успешно добавлен\n')
    except Exception as e:
        print(f'Произошла ошибка при добавлении студента: {e}')
        add_student()


def show_all_students():
    if not students:
        print('Список студентов пуст')
        return
    
    print('\nСписок всех студентов')

    for name, info in sorted(students.items()):
        print(f"Имя: {name}\n Возраст: {info['age']} \n Оценки: {info['grades']}\n")
        


def find_student():
    search_name = input('Введите имя для поиска ').strip()
    if not search_name:
        print('Имя для поиска не может быть пустым')
        return


    for student_name, info in students.items():
        if student_name.lower() == search_name.lower():
            print(f"\nИмя: {student_name}\n Возраст: {info['age']}\n Оценки: {info['grades']}\n")
            break
    else:
        print('Студент не найден')


def delete_student():
    deleiting_name = input('Введите имя студента для удаления ').strip()
    if not deleiting_name:
        print('Имя для удаления не может быть пустым')
        return

    if deleiting_name in students:
        del students[deleiting_name]
        print(f'Студент {deleiting_name} успешно удален')
    else:
        print('Студент не найден')

def add_grade():
    

    student_name = input('Введите имя студента ')
    if not student_name:
        print('Имя не может быть пустым')
        return
    
    if student_name not in students:
        print(f'Студент с именем {student_name} не найден')
        return
    
    try:
        grade = int(input('Введите оценку от 2-5: '))
        if grade < 2 or grade > 5:
            print('Оценка должна быть от 2 до 5')
            return
        
        students[student_name]['grades'].append(grade)
        print(f'Оценка {grade} добавлена студенту {student_name}')

    except Exception as e:
        print(f'Произошла ошибка при добавлении оценки: {e}')


def show_older_students_than():
    try:
        min_age = int(input('Введите минимальный возраст: '))
        if min_age <= 0 or min_age > 100:
            print("Возраст должен быть от 1 до 100 лет!")
            return
        
        print(f'\n Студенты старше {min_age} лет:')

        count = 0
        for name, info in sorted(students.items()):
            if info['age'] >= min_age:
                print(f"Имя:{name}\n, Возраст:{info['age']}\n, Оценки:{info['grades']}\n")
                count += 1

        if count == 0:
            print(f'Студенты старше {min_age} не найдены')


    except Exception as e:
        print(f'Произошла ошибка при добавлении оценки: {e}')


def show_top_students():

    try:
        min_average = float(input('Введите минимальный балл: '))

        print(f"\nСтуденты со средним баллом выше {min_average}:")
        count = 0

        for name, info in students.items():
            if info['grades']:
                average_grade = sum(info['grades'])/len(info['grades'])
                if average_grade > min_average:
                    print(f"\n Имя:{name}, \n Возраст:{info['age']}, \n Оценки:{info['grades']}, \n Средний балл:{average_grade} ")
                    count += 1

        if count == 0:
            print(f'Студенты со средним баллом выше {min_average}не найден')


    except Exception as e:
        print(f'Произошла ошибка при добавлении оценки: {e}')



def export_to_csv():
    filename = input('Введите имя файля для сохранения: ').strip()
    if not filename:
        print('Имя файла не может быть пустым ')
        return
    filename += '.csv'

    try: 
        with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
            writer = csv.writer(file, delimiter = ';')
            writer.writerow(['Имя', 'Возраст', 'Оценки'])
            for name, info in students.items():
                grades_str = ','.join(map(str, info['grades']))
                writer.writerow([name, info['age'], grades_str])
        print('Данные успешно экспортированы')
    except Exception as e:
        print(f'Ошибка при экспорте {e}')

def import_from_csv():
    filename = input('Введите имя файля для импорта: ').strip()
    if not filename:
        print('Имя файла не может быть пустым ')
        return
    filename += '.csv'
    if not os.path.exists(filename):
        print('Файла с таким именем не существует')
        return{}
    students = {}
    imported_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
    
            for row in reader:
                if len(row) < 3:
                    continue

                name = row[0].strip()
                try:
                    age = int(row[1])
                    grades = [int(grade) for grade in row[2].split(',')] if row[2] else []
                    #Проверка данных
                    valid_grades = all(2<=grade<=5 for grade in grades)
                    if age > 0 and age <= 100 and valid_grades:
                        students[name] = {'age': age, 'grades': grades}
                        imported_count += 1
                except Exception as e:
                    print(f'Произошла ошибка: {e}')

        print(f'импортировано {imported_count} студентов из файла {filename}')
        return students
        

    except Exception as e:
        print(f'Произошла ошибка {e}')
    
def exiting():
    print('Спасибо за использование системы')
    return

variations_of_choice = {
    '1': add_student,
    '2': show_all_students,
    '3': find_student,
    '4': delete_student,
    '5': add_grade,
    '6': show_older_students_than,
    '7': show_top_students,
    '8': export_to_csv,
    '9': import_from_csv,
    '10': exiting
}

def main_menu():
    print('\nДобро пожаловать в систему управления студентами\n')
    print('1. Добавить студента')
    print('2. Показать всех студентов')
    print('3. Найти студента по имени')
    print('4. Удалить студента')
    print('5. Добавить оценку студенту')
    print('6. Студенты старше возраста')
    print('7. Студенты с высокой успеваемостью')
    print('8. Сохранить в файл')
    print('9. Загрузить из файла')
    print('10. Выход')

    choice = input('Выберите действие: ')
    if choice in variations_of_choice:
        variations_of_choice[choice]()
        main_menu()
    else:
        print('Некоректный выбор')
        main_menu()


if __name__ == "__main__":
    main_menu()
