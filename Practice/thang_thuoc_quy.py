# quý 1 tháng 1,2,3
# quý 2 tháng 4,5,6
# quý 3 tháng 7,8,9
# quý 4 tháng 10,11,12

month = int(input('Nhập vào tháng: '))
if month in(1,2,3):
    print(f"Tháng {month} thuộc quý 1")
elif month in(3,4,5):
    print(f"Tháng {month} thuộc quý 2")
elif month in(7,8,9):
    print(f"Tháng {month} thuộc quý 3")
elif month in(10,11,12):
    print(f"Tháng {month} thuộc quý 4")
else:
    print("Tháng không hợp lệ")
