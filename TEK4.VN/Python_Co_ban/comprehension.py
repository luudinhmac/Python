input_list = range(20)
  
output_list = []
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
  
print("Output List using for loop:", output_list)

one_line = [i for i in input_list if i%2==0]
print("Output list using comprehension",one_line)


#ex2
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print("Output List using for loop:", output_list)

comprehension_ex2 = [var**2 for var in range(1, 10)]
print("Output List using comprehension:",comprehension_ex2)

#Tinh so tien phai tra sau sai khi da cong voi thue
#  VAT 8% cua don hang sieu thi
number = [1.09, 23.56, 57.84, 4.56, 6.78]
rate = 0.08
def get_price_with_tax(tax):
    return tax*(1+rate)
s = 0
for i in number:
    s+=get_price_with_tax(i)
print("Sum using for loop:",s)
one_line = [get_price_with_tax(i) for i in number ]
print("Sum using comprehension:",sum(one_line))


#Chuan hoa gia ca trong co so du lieu
original_prices = [3.12, -2.32, 12.12, 13.14, -6.43]
prices = [i  if i >0 else 0 for i in original_prices ]
print(prices)


# set 
quote = "Python is easy"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

# ex 6
# in ra mot tu dien voi khoa la gia tri nguyen tu 0 den 9 
# va gia tri tuong ung voi moi khoa la binh phuong cua khoa do:
ex6 = { i:i**2 for i in range(10)}
print("ex6", ex6)
print(type(ex6))