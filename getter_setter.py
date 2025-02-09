# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#
#     @property
#     def name(self):
#         if self.__name[-1] in "aA":
#             return f'She name is {self.__name}'
#         return f'He name is {self.__name}'
#
#     @property
#     def age(self):
#         return self.__age
#
# nurbol = Student("Nurbol", 17)
#
# print(nurbol.name)
# print(nurbol.age)

# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         if self.__name[-1] in "aA":
#             return f'She name is {self.__name}'
#         return f'He name is {self.__name}'
#
#     @property
#     def age(self):
#         if self.__age < 18:
#             return "Вы несовершеннолетний"
#         return "Вы совершеннолетний"
#
# nurbol = Student("Nurbol",18)
# print(nurbol.age)


# @name.setter
# def name(self, name):
#     self.__name = name
#
#
# @age.setter
# def age(self, age):
#     self.__age = age



# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return f"Ваш баланс {self.__balance}"
#     @balance.setter
#     def balance(self,value):
#         if value >= 0:
#             self.__balance = value
#         else:
#             print("Неправильный баланс")
#
# bank = Bank(100)
# bank_1 = Bank(200)
#
# print(bank.balance)
# print(bank_1.balance)


#task 1

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         if value == "":
#             print("Имя не может быть пустым")
#         self.__name = value
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value <0:
#             print("Возраст не может быть отрицательным")
#
# p =Person("Ivan", 25)
# print(p.name)
# print(p.age)
# p.name = "Nurbol"
# p.age = -5


#task 2

# class Animal:
#     def make_sound(self):
#         return "Живитное издает звук"
# class Dog(Animal):
#     def make_sound(self):
#         return "Собака лает"
# a = Animal()
# print(a.make_sound())
# d = Dog()
# print(d.make_sound())


#task 3

# class Employee:
#     def __init__(self,salary):
#         self.__salary = salary
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self,value):
#         if value < 10000:
#             print("Зарплата не может быть меньше 10 000!")
#         self.__salary = value
# class Manager(Employee):
#     def __init__(self,salary,bonus):
#         Employee.__init__(self, salary)
#         self.bonus = bonus
#
#
# e = Employee(12000)
# print(e.salary)
# e.salary = 5000
#
# m = Manager(15000,5000)
# print(m.salary)
# print(m.bonus)

