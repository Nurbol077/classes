# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         return ">>>" + self.name
#
#
# class B(A):
#     def display(self):
#         return super().show() + "<<<"
#
#
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def make_sound(self):
#         return "Жаныбар ун чыгарат"
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Ит урот"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мышык мыелойт"

# ob_1 = Animal("Object 1")
# ob_2 = Animal("Object 2")
#
# gans = Dog("Gans")
# balto = Dog("Balto")
#
# muiza = Cat("Muiza")
# akusia = Cat("Akusia")
#
# animals = [ob_1, ob_2, gans, balto, muiza, akusia]
#
# for animal in animals: # animal = gans
#     print(animal.make_sound())
#     print("#" * 10)


# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def info(self):
#         raise NotImplementedError("Бул функцияны иштеткенге болбойт")
#
# class Student(Person):
#     def info(self):
#         print(f"Hello, I'm {self.name} and I'm student!!")
#
# class Teacher(Person):
#     pass
#
# nurbol =Student("Nurbol")
# arsen =Teacher("Arsen")
#
# for person in [nurbol,arsen]:
#     try:
#         person.info()
#     except (NotImplementedError, ValueError):
#         print("Бул класстын ичине info деген функция жаз")








