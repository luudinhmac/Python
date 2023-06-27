x=float(input())
i =1
s =float(0)
while abs((((-1)**(i+1))/i)*(x**i))  >= 1e-5:
    s += (((-1)**(i+1))/i)*(x**i)
    i+=1
print(f"Value of: ln(x+1) với x = {x} is: {s}")