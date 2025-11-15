from abc import ABC, abstractmethod
import math
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimetr(self):
       pass
    
    def info(self):
        return "Фигура"
    

class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def calculate_area(self):
        return self.side **2
    
    def calculate_perimetr(self):
        return self.side * 4
    
    def info(self):
        return "Квадрат"
    
    def __str__(self):
        return f"Квадрат со стороной {self.side}"
    
    def __len__(self):
        return self.calculate_perimetr()
    
    def __eq__(self, other_value):
        if not isinstance(other_value, Square):
            return NotImplemented
        return self.calculate_area() == other_value.calculate_area()
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimetr(self):
        return math.pi * self.radius * 2
    
    def info(self):
        return "Круг"
    
    def __str__(self):
        return f"Раидус круга равен {self.radius}"
    
    def __len__(self):
        return self.calculate_perimetr
    
    def __eq__(self, other_value):
        if not isinstance(other_value, Circle):
            return NotImplemented
        return self.calculate_area == other_value.calculate_area()
    

class Geometry_calculator:
    @staticmethod
    def validate_positive(number):
        if number > 0:
            return True
        return False
    
    @staticmethod
    def calculate_diagonal(lenght, widht):
        if lenght < 0 or widht < 0:
            raise ValueError("Длина и ширина должны быть положительными")
        return math.sqrt(widht**2 + lenght**2)
    
    @staticmethod
    def is_larger(shape1, shape2):        #shape1 sahpe2 экземляры класса Square/Circle
        area1 = shape1.calculate_area()
        area2 = shape2.calculate_area()
        if area1 > area2:
            return shape1
        elif area2 > area1:
            return shape2
        else:
            return None #равны
        

square1 = Square(4)
circle1 = Circle(5)
print(f"\nПлощадь квадрата: {square1.calculate_area()}")
print(f"\nПлощадь круга: {circle1.calculate_area()}")

print(f"\n:Периметр {square1.calculate_perimetr()}")
print(f"\nПериметр круга: {circle1.calculate_perimetr()}")

print(f"{square1.info()}")
print(f"{circle1.info()}")

print(f"{square1.__str__()}")
print(f"{circle1.__str__()}")

print(f"{square1.__len__()}")

square3 = Square(4)
print(f"{square1.__eq__(square3)}")

print(f"{Geometry_calculator.validate_positive(5)}")
print(f"{Geometry_calculator.calculate_diagonal(4,5)}")

square3 = Square(6)
square4 = Square(8)
print(f"{Geometry_calculator.is_larger(square3, square4)}")
