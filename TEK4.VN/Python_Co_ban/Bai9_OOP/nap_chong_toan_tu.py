class vi_du:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        return a, b 
    # def __str__(self):
    #     return "{0},{1}".format(self.x, self.y)
    def __eq__(self, other):
        c = abs(self.x) + abs(self.y)
        d = abs(other.x) + abs(other.y)
        return c == d
    
    
t1 = vi_du(5, 4)
t2 = vi_du(5, 8)
print(t1+t2)
t3 = vi_du(5, 9)
t4 = vi_du(7,10)
print(t3==t4)
