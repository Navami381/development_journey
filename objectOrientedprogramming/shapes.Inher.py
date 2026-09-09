"""
Common 2D Shapes and Formulas
Rectangle:Multiply length (l) by width (w) (A = l × w)
Square: Multiply the side length (a) by itself (A = a²)
Circle: Multiply pi (π) by the radius squared (A = π r²)
Parallelogram: Multiply base (b) by vertical height (h) (A = bh).
Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two (\(A = \frac{1}{2}(a + b)h\)).

"""
class Shape:
    name:str

    def __init__(self,name):
        self.name=name

class Rectangle(Shape):
    length:int
    width:int
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def area(self):
        print("area of",self.name,"=",self.length*self.width)

class Square(Shape):
    length:int
    def __init__(self,name,length):
        super().__init__(name)
        self.length=length
    def area(self):
         print("area of",self.name,"=",self.length**2)

class Circle(Shape):
    radius:float
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        print("area of",self.name,"=",3.14*(self.radius**2))

class Parallelogram(Shape):
    base:int
    height:int
    def __init__(self,name,base,height):
        super().__init__(name)           #calling parent class constructor
        self.base=base
        self.height=height
    def area(self):
        print("area of",self.name,"=",self.base*self.height)

class Trapezium(Shape):
    a:int
    b:int
    height:int
    def __init__(self,name,a,b,height):
        super().__init__(name)
        self.a=a
        self.b=b
        self.height=height
    def area(self):
        print("area of",self.name,"=",((self.a+self.b)*self.height)/2)

r_instance=Rectangle("rectangle",7,5)
r_instance.area()

s_instance=Square("square",5)
s_instance.area()

c_instance=Circle("circle",4)
c_instance.area()

p_instance=Parallelogram("parallelogram",10,20)
p_instance.area()

t_instance=Trapezium("trapezium",5,6,7)
t_instance.area()


