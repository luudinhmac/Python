class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def areas(self):
        return self.pi*self.radius*self.radius

    def circumference(self):
        return self.pi*2*self.radius


r = float(input())
circle = Circle(r)
print("PI:", Circle.pi)
print("Radius:", r)
print("Circumference:", circle.circumference())
print("Area:", circle.areas())
