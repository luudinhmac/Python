class Vector:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        if len(self.v) != len(other.v):
            return None
        else:
            a = []
            for i in range(len(self.v)):
                a.append(self.v[i] + other.v[i])
            return a

    def __mul__(self, other):
        if len(self.v) != len(other.v):
            return None
        else:
            tich = 0
            for i in range(len(self.v)):
                tich += self.v[i]*other.v[i]
            return tich


a = [1, 2, 3]
b = [3, 4, 5]

v1=Vector(a)
v2=Vector(b)
print(v1+v2)
print(v1*v2)