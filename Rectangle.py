from GeometricObject import GeometricObject
import math
class Rectangle(GeometricObject):
    def __init__(self,width,height,color,filled):
        super().__init__(color,filled)
        self.__width = width
        self.__height = height
    def getWidth(self):
        return self.__width
    def setWidth(self,width):
        self.__width = width
    def getHeight(self):
        return self.__height
    def setHeight(self,height):
        self.__height = height
    def getArea(self):
        return self.__height * self.__width
    def getPerimeter(self):
        return (self.__width + self.__height) * 2
    def printRectangle(self):
        print(self.__str__() + " width: " + str(self.__width) + " height: " + str(self.__height))
