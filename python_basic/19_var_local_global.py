# Biến toàn cục có tác dụng trong toàn bộ ct
# Biến cục bộ có tác dụng trong 1 phạm vi nhất định

x = 100
def example():
    global x
    x = 10
    print(x)

example()
print(x)