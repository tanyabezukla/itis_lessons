menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100}

def show_menu_sorted():

    a = int(input('1.Вывести меню алфавиту\n2.Вывести меню по возратсанию цены\n Ваш выбор: ').strip())
    if a == 1:
        print('Меню по алфавиту:')
        sorted_by_alphabet = sorted(menu.items(), key = lambda x: x[0])

        for item, price in sorted_by_alphabet:
            print(f"{item}: {price} руб")
            
    elif a == 2:
        print('Меню по возрастанию цены')
        sorted_by_price = sorted(menu.items(), key = lambda x: x[1])

        for item, price in sorted_by_price:
            print(f"{item}: {price} руб")
            
    else:
        print("Введены не верные данные")
        return


 
def average_cost():

    avg = sum(map(lambda x: x[1], menu.items()))/len(menu)
    print(f"Средняя цена блюда {avg} руб")


def add_item():
    new_item = input("Введите название нового блюда: ").strip().lower()
    if not new_item:
        print("Название блюда не может быть пустым ")
        return
    
    try:
        new_item_price = int(input("Введите цену нового блюда: "))
        if new_item_price <= 0:
            print("Цена должна быть положительной ")
            return
        
        update_menu = lambda d, p: menu.update({d: p})
        update_menu(new_item, new_item_price)
        print(f"Новая позиция {new_item} добавлена в меню по цене {new_item_price} руб\n")


    except ValueError:
        print("Ошибка: введите корректную цену ")
        add_item()
    
    
def remove_item():
    removed_item = input("Введите позицию для удаления: ").strip().lower()
    if removed_item in menu:
        del menu[removed_item]
        print(f"Позиция {removed_item} была успешно удалена")
    else:
        print("Позиция не найдена")

def show_cheaper_item_than():
    try:
        max_price = int(input("\nВведите максимальную цену: "))
        filtered = list(filter(lambda x: x[1] < max_price, menu.items()))
        if filtered:
            print(f"\nблюда дешевле: {max_price} руб: ")
            for item, price in filtered:
                print(f"{item}: {price} руб")
        else:
            print(f"Позиций дешевле {max_price} не найдено")

    except ValueError:
        print("Ошибка ввода цены")

def min_max_item():
    min_item = min(menu.items(), key = lambda x: x[1])
    max_item = max(menu.items(), key = lambda x: x[1])
    print(f"Самое дешевое блюдо: {min_item[0]} - {min_item[1]}")
    print(f"Самое дорогое блюд: {max_item[0]} - {max_item[1]}")

def show_drinks():
    drinks = filter(lambda x: x[0] in ['coffee', 'tea', 'juice'], menu.items())
    sorted_drinks = sorted(drinks, key = lambda x: x[1])
    if sorted_drinks:
        print("Напитки по цене:")
        for item, price in sorted_drinks:
            print(f"{item}: {price} руб")
    else:
        print("Напитки не найдены в меню")


def make_order():
    from functools import reduce
    order_input = input("Введите блюда через запятую: ")
    items = list(map(lambda x: x.strip().lower(), order_input.split(',')))

    #Проверяем наличи блюд в меню
    valid_items = list(filter(lambda x: x in menu, items))

    #Сосатвлеям словарь 
    #order_dict = {item: menu[item] for item in valid_items}

    order_dict = dict(map(lambda x: (x, menu[x]), valid_items)) #menu[x]-цена
    if not order_dict:
        print("Вы ничего не выбрали или таких позиций нет в меню")
        return
    
    total_price = reduce(lambda x,y: x+y, order_dict.values(), 0)

    print("\nВаш заказ: ")
    list(map(lambda item: print(f"{item[0]}. {item[1][0]} - {item[1][1]}руб"), enumerate(order_dict.items(), start=1 )))
    print(f"Итого: {total_price} руб.")


    if total_price > 500:
        print("Поздравляем, у вас скидка 10%!")
        discount = total_price * 0.1
        print(f"К оплате: {total_price - discount} руб")

variatoins_of_choice = {
    '1' : show_menu_sorted,
    '2' : average_cost,
    '3' : add_item,
    '4' : remove_item,
    '5' : show_cheaper_item_than,
    '6' : min_max_item,
    '7' : show_drinks,
    '8' : make_order
}

def main_page():
    print("\n1.Вывести все меню")
    print("2.Средняя цена блюда в меню")
    print("3.Добавить новое блюдо в меню")
    print("4.Удалить блюдо из меню")
    print("5.Показать все блюда дешевле определенной цены")
    print("6.Вывыести самое дешевое и дорогое блюдо")
    print("7.Сделать список только напитков")
    print("8.Сделать заказ")

    choice = input("\nВыберите действие: ")
    if choice in variatoins_of_choice:
        variatoins_of_choice[choice]()
        main_page()
    else:
        print('Некоректный выбор')
        main_page()


if __name__ == "__main__":
    main_page()
