n = int(input())
if n <0:
    print("Factorial does not exist for negative numbers")
else:
    if n <=1:
        print(f"The factorial of {n} is 1")
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial= factorial*i
        
        print(f"The factorial of {n} is {factorial}")
