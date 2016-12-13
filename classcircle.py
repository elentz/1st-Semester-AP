class Circle:
    def __init__(self, radius):
        self.r=radius
    def area(self):
        return self.r**2*3.14

    def circumference(self):
        return self.r*2*3.14

x = Circle(10)
print x.area(), x.circumference()
