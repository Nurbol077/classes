# """
# публичный - public ->
# приватный - private -> __
# защищенный - protected -> _
#
# """
#
#
# class Shape:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         return self.__width * self.__height
#
#     def perimeter(self):
#         return 2 * (self.__width + self.__height)
#
#
# shape_1 = Shape(10, 20)
# print(shape_1.area())
# print(shape_1.perimeter())



# task 1

# class BankAkkount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, amount):
#         if amount >=0:
#             self.__balance = amount
#         else:
#             print("Баланс не изменится")
#
# account = BankAkkount(1000)
# print(account.get_balance())
# account.set_balance(500)
# print(account.get_balance())
# account.set_balance(-200)
# print(account.get_balance())


# task 2

# class Student:
#     def __init__(self,age=0):
#         self.__age = age
#     def get_age(self):
#         return self.__age
#     def set_age(self,value):
#         if value >= 0:
#             self.__age =value
#         else:
#             print("Возраст не изменится")
# student =Student(20)
# print(student.get_age())
# student.set_age(25)
# print(student.get_age())
# student.set_age(-5)
# print(student.get_age())


# task 3

# class Car:
#     def __init__(self, speed=0):
#         self.__speed = speed
#
#     def get_speed(self):
#         return self.__speed
#
#     def set_speed(self, value):
#         if 0 <= value <= 300:
#             self.__speed = value
#         else:
#             print("Скорость не изменяется")
#
# car = Car(60)
# print(car.get_speed())
# car.set_speed(120)
# print(car.get_speed())
# car.set_speed(350)
# print(car.get_speed())

# task 4

# class User:
#     def __init__(self,password):
#         self.__passwod = password
#     def get_password(self):
#         return self.__passwod
#     def set_password(self,new_password):
#         if len(new_password) >= 6:
#             self.__passwod = new_password
#         else:
#             print("Пароль не изменится")
# user = User("secret123")
# print(user.get_password())
# user.set_password("12345")
# print(user.get_password())
# user.set_password("newpassword")
# print(user.get_password())

# task 5

# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius
#
#     def get_celsius(self):
#         return self.__celsius
#
#     def set_celsius(self, value):
#         self.__celsius = value
#
#     def get_fahrenheit(self):
#         return self.__celsius * 9 / 5 + 32
#
#
# temp = Temperature(25)
# print(temp.get_celsius())
# print(temp.get_fahrenheit())
# temp.set_celsius(-300)
# print(temp.get_celsius())
# temp.set_celsius(30)
# print(temp.get_celsius())
# print(temp.get_fahrenheit())


