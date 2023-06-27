# Nhập vào năm dương lịch, kiểm tra xem năm đó có phải là năm nhuận hay không



def leapyear(year):

    if (year % 4 ==0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False 
if __name__=='__main__':
    year = int(input("Nhập năm: "))
    y = leapyear(year)
    if y == True:
        print(f"{year} là Năm Nhuận")
    else:
        print(f"{year} Không phải năm nhuận")