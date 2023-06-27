# move zero to the right side
# input_s = [0, 1, 2, 5, 7, 0, 9]


# def move_zero_right(input_s):
#     n = len(input_s)
#     if n==0:
#         return []
#     k =0
#     for i in range(n):
#         if input_s[i]!=0:
#             input_s[k]=input_s[i]
#             k+=1

#     for j in range(k,n):
#         input_s[j]= 0
#     return input_s

# print(move_zero_right(input_s))

# class Item():
#     def __init__(self, name: str, price: float, quantity=0):
#         self.names = name
#         self.price = price
#         self.quantity = quantity

#         assert price >= 0
#         assert quantity >= 0

#     def tong(self):
#         return self.price * self.quantity

#     @staticmethod
#     def check(gia):
#         if gia > 10:
#             return ("Expensive")
#         else:
#             return ("Chip")


# # init child class
# class Phone(Item):
#     def __init__(self, name: str, price: float, quantity=0, type_='4G'):
#         super().__init__(name, price, quantity)
#         self.type = type_


# item1 = Item("phone", 10, 10)
# item2 = Item("Laptop", 20, 20)
# item3 = Item("Tivi", 30)

# phone1 = Phone("Phone 1", 1000, 2)
# phone2 = Phone("Phone 2", 2000, 2, '5G')
# print(phone2.type)
# gt =1
# n = 3
# for i in range(1,n+1):
#     gt*=i
# print(gt)



# def mywraper(func):
#     def myInternal():
#         print("insize ")
#         func()
#     return myInternal
# @mywraper
# def myfunc():
#     print("hello")

# myfunc()



