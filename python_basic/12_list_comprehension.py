# list comprehension: giúp lấy ra 1 list phần tử theo mong muốn, code ngắn gọn, dễ đọc, dễ nhìn
# new_list[<action> for in <iterator> if <some condition>]

#hello = "Hello, world!"
#for x in hello:
#    print(x)

#print([char for char in hello])
#print([number for number in range(0,10) if number % 2 ==0])

VAT = 0.10
list_price = [100,120,200,300]
def price_product(price):
    return price*(1+VAT)
print([price_product(price) for price in list_price])