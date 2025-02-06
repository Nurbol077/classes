"""
публичный - public ->
приватный - private -> __
защищенный - protected -> _

"""


class Shape:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


shape_1 = Shape(10, 20)
print(shape_1.area())
print(shape_1.perimeter())

