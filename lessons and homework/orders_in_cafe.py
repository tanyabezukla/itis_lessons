class Product:
    def __init__(self, name, calories_per_100):
        self.name = name
        self.calories_per_100 = calories_per_100

class Menuitem(Product):
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        
    def calories(self):
        total_calories = 0
        for product, grams in self.ingredients:
            total_calories += (product.calories_per_100 * grams)/100
        return total_calories
    
class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_items(self, menu_item):
        self.items.append(menu_item)

    def total_price(self):
        return sum(item.price for item in self.items)
    

bread = Product("Bread", 300)
cheese = Product("Cheese", 250)
tomato = Product("Tomato", 50)

sandwich = Menuitem("sandwich", 300, [(bread, 70), (cheese, 50), (tomato, 30)])
coffee = Menuitem("coffee", 150, [])

customer = Customer("Sofia")

order = Order(customer)
order.add_items(sandwich)
order.add_items(coffee)

print(f'\nclient: {order.customer.name}')
for item in order.items:
    calories = item.calories()
    print(f'{item.name}: {item.price} rub. {calories}')

print(f'total price: {order.total_price}')
