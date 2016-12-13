class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius**2)*3.14

    def perimeter(self):
        return 2*self.radius*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.radius, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return (2* self.x) + (2 * self.y)

    def __str__(self):
        return "Rectangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x

class RightTriangle():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def area(self):
        return (.5*(self.x * self.y))

    def perimeter(self):
        return ((self.x ** 2 + self.y ** 2) ** .5) + self.x + self.y

    def __str__(self):
        return "Right Triangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Iso(RightTriangle):
    def __init__(self, x):
        self.x = x
        self.y = x

class Depth():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def surfacearea(self):
        return 2 * self.area() + self.z * (self.perimeter())

    def volume(self):
        return self.area() * self.z

class Box(Rectangle, Depth):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Cube(Square, Depth):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x

class Wedge(RightTriangle, Depth):
        def __init__(self, x,y,z):
            self.x = x
            self.y = y
            self.z = z




x = Rectangle(3,4)
print x
y = Square(5)
print y
z = RightTriangle(3,4)
print z
a = Iso(4)
print a
c = Box(3,4,5)
print c.surfacearea()
print c.volume()
d = Cube(3)
print d.surfacearea()
print d.volume()
e = Wedge(3,4,5)
print e.surfacearea()
print e.volume()
