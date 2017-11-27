import math

class Rectangle:
    # Construct a circle object
    def __init__(self, width = 1,height = 2):
        self.width = width
        self.height = height

    def getPerimeter(self):
        return 2* (self.width) * 2(self.height)

    def getArea(self):
        return self.width * self.height

    def setHeight(self, height):
        self.height = height

    def setWidth(self, width):
        self.width = width


def main():
    rectangle1 = Rectangle(4,40)
    print(rectangle1.width, rectangle1.height, rectangle1.getArea())

main()