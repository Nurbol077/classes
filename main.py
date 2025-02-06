# class Animal:
#     name = "Cat"
#     age = 1
#
#     def eat(self):
#         print("Eating...")
#
#     def sleep(self):
#         print("Sleeping...")
#
#     def run(self):
#         print("Running...")
#
#
# obj_1 = Animal()
# print(obj_1.name)
# print(obj_1.age)
# obj_1.eat()
# obj_1.sleep()
# obj_1.run()


# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f'Name; {self.name}')
#         print(f'Surname; {self.surname}')
#         print(f'Age; {self.age}')
#         print('#' * 20)
#
#
#
# person_1 = Person("Arsen", "Kenzhegulov", 22)
# person_2 = Person("Nurbol", "Kadyrbekov", 17)
# person_3 = Person("Emir", "Kachkynov", 13)
# person_4 = Person("Asylbek", "Arstanbekov", 14)
# person_5 = Person("Ainagul", "Azhybaeva", 38)
# person_6 = Person("Elnara", "Kasymbekova", 15)
# person_7 = Person("mirzhana", "Begalieva", 15)
#
# users = [person_1, person_2, person_3, person_4, person_5, person_6, person_7]
# for user in users:
#         user.info()



"""
getattr(obj, name [, default]) — возвращает значение атрибута объекта;
hasattr(obj, name) — проверяет на наличие атрибута name в obj;
setattr(obj, name, value) — задает значение атрибута (если атрибут не существует, то он создается);
delattr(obj, name) — удаляет атрибут с именем name.
"""


class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

car_1 = Car("BMW", 2018)
print(car_1.model)
print(car_1.year)
setattr(car_1,"color","red")

if hasattr(car_1, "color"):
    print(car_1.color)
else:
    print("Invalid attribute")

# print(getattr(car_1,"model"))
# print(getattr(car_1,"year"))
# print(getattr(car_1,"color", "Invalid atribute"))

delattr(car_1,"color")