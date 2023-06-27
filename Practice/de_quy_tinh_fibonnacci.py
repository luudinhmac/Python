# F1 =1 , F2 =2 , Fn = F(n-1) + F(n-2)
def fibonacci(n):
    if n<0:
        return -1
    if n== 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(n):
    for i in range(1,n):
        print(fibonacci(i), end=" ")


print_fibonacci(10)
