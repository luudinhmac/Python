a,b,*other = (1,2,3,4,5,6,7,8,9,10,11)
print(a,b)
print(other)
r, *g, other = (192, 210, 100, 0.5)
print(g)
*r, g, other = (192, 210, 100, 0.5)
print(r)
*r, g, other1, other2 = (192, 210, 100, 0.5)
print(r)
*r,g,other1,other2, other3 = (192, 210, 100, 0.5)
print(r)

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
print(numbers)


def powers(number):
    return number, number ** 2, number ** 3
result = powers(2)
print(result)
number,square,cube=powers(2)
print(number)
print(square)
print(cube)


# Tinh fibonacci bang ky thuat unpacking

def fibonacci(n):
    f0,f1 =1,1
    for i in range(n):
        f0,f1 = f1,f0+f1
    print (f0)

fibonacci(8)

def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    print(a)

fib(4)


points=[(1.2,1.5),(-3.1,5.6),(4.5,2.6),(1.4,6.8),(2.1,-8.4)]
print("Unpacking for loop..." )
print(points[1])
distance = lambda point: abs(point[0]) + abs(point[1])
points.sort(reverse = True, key = distance)
print(points)
print(f"{points[0]} has max distance to O(0,0): {distance(points[0])} ")

