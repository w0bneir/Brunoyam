# class Car():
#     color = "black"
#     wheels = 4
#     count_door = 5
#     def ride(self):
#         print("Машина поехала")
#     def clac(self, a, b):
#         print("Машина сигналит")
#         return a * b
#     def mult(self):
#         print(self.wheels * self.count_door)
# c1 = Car()
# c1.color = "yellow"
# # print(f'Цвет первой машини: {c1.color}')
# # print(f'Колес у первой машины: {c1.wheels}')
# c1.mult()
#
# c2 = Car()
# c2.wheels = 5
# # print(f'Цвет второй машини: {c2.color}')
# # print(f'Колес у второй машины: {c2.wheels}')
# c2.mult()
# class Phone:
#     def __init__(self, brand, model, price, height, width):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.height = height
#         self.width = width
#     def current_discount(self, amount_of_disconut):
#         self.price -= amount_of_disconut
#         print(f"Цена {self.brand} {self.model} со скидкой: {self.price}")
#     def diagonal(self):
#         print(f"Диагональ {self.brand} {self.model}: {(self.height ** 2 + self.width ** 2) ** 0.5 / 2.54 / 100 * 93 / 10}")
# phone1 = Phone('Goggle', 'Pixel 6', 30000, 158.6, 74.8)
# phone1.current_discount(5000)
# phone1.diagonal()
#
# class Animal:
#     height = 10
#     weight = 20
#     color = ""
#     area = ""
#     def eat(self):
#         print("Животное ест")
#     def step(self):
#         print("Животное идет")
# class Cat(Animal):
#     tail_lenght = 10
#     fur = True
#     Breed = ""
#     def voice(self):
#         print("Meow")
#     def jump(self):
#         print("Jump")
# c1 = Cat()
# c1.height = 5
# c1.weight = 5
# c1.color = "Black"
# c1.eat()
# class Animal:
#     def eat(self):
#         print(f"{self.name} ест.")
# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} мяукает.")
# my_cat = Cat()
# my_cat.name = "Мурзик"
# my_cat.color = "черный"
# my_cat.eat()
# my_cat.meow()