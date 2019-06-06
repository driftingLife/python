from GeometricObject import GeometricObject
import math
class Circle(GeometricObject):
    def __init__(self,radius,color,filled):
        super().__init__(color,filled)
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def setRadius(self,radius):
        self.__radius = radius
    def getArea(self):
        return self.__radius * self.__radius  * math.pi
    def getPerimeter(self):
        return 2 * self.__radius * math.pi
    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))