class Vector:
    def __init__(self, point):
        self.point = point

    def __add__(self, other):
        if len(self.point) != len(other.point):
            print("Size Error!")
            return None
        r = []
        for i in range(len(self.point)):
            r.append(self.point[i] + other.point[i])
        return r

    def __sub__(self, other):
        if len(self.point) != len(other.point):
            print("Size Error!")
            return None
        r = []
        for i in range(len(self.point)):
            r.append(self.point[i] - other.point[i])
        return r

    def __mul__(self, other):
        if len(self.point) != len(other.point):
            print("Size Error!")
            return None

        r = []
        for i in range(len(self.point)):
            r.append(self.point[i] * other.point[i])
        return sum(r)

    def __eq__(self, other):
        if len(self.point) != len(other.point):
            print("Size Error!")
            return None
        f = True
        for i in range(len(self.point)):
            if self.point[i] != other.point[i]:
                f = False
        return f


vector1 = Vector([float(x) for x in input().split()])
vector2 = Vector([float(x) for x in input().split()])

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector1 == vector2)
