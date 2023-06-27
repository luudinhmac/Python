# Tháng 1,3,5,7,8,10,12 có 31 ngày
# Tháng 4,6,9,10,11 có 30 ngày
# Tháng 2 thì yêu cầu nhập thêm năm, nếu năm nhuận có 29 ngày, không nhuận 28 ngày
import leap_year
month = int(input("Nhập vào tháng:"))
if month in (1,3,5,7,8,10,12):
    print(f"Tháng {month} có 31 ngày")
elif month in(4,6,9,11):
    print(f"Tháng {month} có 30 ngày")
elif month ==2:
    year = int(input("Nhập năm:"))
    if leap_year.leapyear(year) == True:
        print(f"Tháng {month} có 29 ngày")
    else:
        print(f"Tháng {month} có 28 ngày")
else:
    print("Tháng không hợp lệ!")