def square_number(n):
    L =[]
    
    for i in range(n+1):
        for j in range(i+1):
            if j**2 == i:
                L.append(i)
    return L
n = int(input())
print (square_number(n))