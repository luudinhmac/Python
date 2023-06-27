
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # method
    # perimeter
    def perimeter(self):
        return 2*(self.width + self.length)
    # area
    def area(self):
        return self.length*self.width
    # Show info rectangle
    def display(self):
        print(f"The length of rectangle is: {self.length}")
        print(f"The width of rectangle is: {self.width}")
        print(f"The perimeter of rectangle is: {self.perimeter()}")
        print(f"The area of rectangle is: {self.area()}")


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


length = float(input())
width = float(input())
myRectangle = Rectangle(length, width)
myRectangle.display()
height = float(input())
myParallelepipede = Parallelepipede(length, width, height)
print(f"The volume of myParallelepipede is: {myParallelepipede.volume()}")

