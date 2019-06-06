from Circle import Circle
from Rectangle import Rectangle

def main():
    c1 = input()
    r1 = input()
    r2 = input()
    cC = input()
    cF = input()
    rC = input()
    rF = input()
    cir = Circle(c1,cC,cF)
    rect = Rectangle(r1,r2,rC,rF)
    print("Circle:")
    print("Radius is ",cir.getRadius())
    print("Diameter is ",2 * cir.getRadius())
    print("Area is ", cir.getArea())
    print("Perimeter is ",cir.getPerimeter())
    c.printCircle()


main()
