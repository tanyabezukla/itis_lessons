books = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1966},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"id": 3, "title": "Война и мир", "author": "Толстой", "year": 1869},
    {"id": 4, "title": "Анна Каренина", "author": "Толстой", "year": 1877},
    {"id": 5, "title": "Собачье сердце", "author": "Булгаков", "year": 1925}
]

def find_book_by_title():
    user_title = input("Введите название книги: ").strip().lower()
    if not user_title:
        print("Вы ничего не ввели")
        find_book_by_title()

    index = -1
    for i in range(len(books)):
        if (books[i]['title']).lower() == user_title:
            index = i
            break
    if index != -1:
        found_book = books[index]
        print(f"Найдена книга: {found_book['title']}, {found_book['author']}, {found_book['year']}")
    else:
        print(f"Кгига под названием: {user_title} не найдена, убедитесь в правильности написания названия книги")


def find_books_by_author():
    print('Поиск книг автора')
    user_author = input('Введите Фамилию автора: ').strip().lower()
    if not user_author:
        print('Вы ничего не ввели')
        find_books_by_author

    result = []
    for book in books:
        if book['author'].lower() == user_author:
            result.append(book)

    if result:
        print('Найдены книги: ')
        for j in result:
            print(f"{j['title']}, {j['author']}, {j['year']}")

    else:
        print(f'Книги автора {user_author} не найдено')


def sort_books_by_year():
    books_copy = books.copy()
    n = len(books_copy)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if books_copy[j]['year'] > books_copy[j+1]['year']:
                books_copy[j], books_copy[j+1] = books_copy[j+1], books_copy[j]
                swapped = True

        if not swapped:
            break

    print('Книги по возрастанию года: ')
    for i, book in enumerate(books_copy, 1):
        print(f"{i}. {book['title']} {book['author']}, {book['year']}")
   



def filter_books_by_year_range():
    start_year = int(input("Введите начальный год: "))
    end_year = int(input("Введите конечный год: "))

    if not start_year or not end_year:
        print("Вы не ввели одно из значений ")
        filter_books_by_year_range()

    result = []

    for book in books:
        if start_year <= book['year'] <= end_year:
            result.append(book)

    if result:
        for a,b in enumerate(result, 1):
            print(f"{a}. {b['title']} {b['author']} {b['year']}")

    else: 
        print("Книги в диапозоне {start_year} - {end_year} не найдены")



variations_of_choice = {
    "1": find_book_by_title,
    "2" : find_books_by_author,
    "3" : sort_books_by_year,
    "4" : filter_books_by_year_range
}

def main_page():
    print("Главная страница")
    print("1. Найти книгу по названию ")
    print("2. Найти книгу по  автору ")
    print("3. Отсортировать книги по годам")
    print("4. Найти книги по диапозону лет ")

    choice = input("Выберите действие: ").strip()
    if choice in variations_of_choice:
        variations_of_choice[choice]()
        main_page()
    else:
        print("Некоректный выбор")
        main_page()

if __name__ == "__main__":
    main_page()
