#FYCS _20
class Polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.side=[0 for i in range (no_of_sides)]
    def inputsides(self):
        self.sides=[float(input("Enter side"+str(i+1)+":"))for i in range(self.n)]

    def dispsides(self):
        for i in range(self.n):
            print("Sides", i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is%0.2f "%area)
t=Triangle()
t.inputsides()
t.dispsides()
t.findArea()
            
