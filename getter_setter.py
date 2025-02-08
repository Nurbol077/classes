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



class Bank:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return f"Ваш баланс {self.__balance}"
    @balance.setter
    def balance(self,value):
        if value >= 0:
            self.__balance = value
        else:
            print("Неправильный баланс")

bank = Bank(100)
bank_1 = Bank(200)

print(bank.balance)
print(bank_1.balance)