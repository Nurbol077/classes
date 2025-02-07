# task 1

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def dislay_info(self):
#         print(f'Brand; {self.brand}')
#         print(f'Model; {self.model}')
#         print(f'Year; {self.year}')
#         return '#' * 20
#
# car_1 = Car("Toyota", "Camry", 2022)
# car_2 = Car("Bmw", "X5", 2021)
# print(car_1.dislay_info())
# print(car_2.dislay_info())

# task 2

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self,amount):
#         if amount>0:
#             self.balance += amount
#             print(self.balance)
#
#
#     def withdraw(self,amount):
#         if amount <= self.balance and amount > 0:
#             self.balance -= amount
#             print(self.balance)
#         else:
#             print("Недостаточно средств")
#
# account = BankAccount("Nurbol", 1000)
# account.deposit(500)
# account.withdraw(500)

# task 3

# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student1 = Student("Айжан", 20, [90, 85, 88, 92])
# print(student1.average_grade())


# task 4

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             return "Ошибка деление на ноль"
#
#
# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(10, 4))
# print(calc.divide(1, 1))
# print(calc.subtract(5, 5))
# print(calc.divide(10, 0))



