# Function

def test():
    print("hello world")
    def test1():
        print("fc1")
    test1()

test()

def func(x, y, z=None):
    print(x,y,z)
    return x + z, x * y
res1, res2 = func(3,9,10)
print(res1,res2)
