"""
ex4: viet ct tim kiem sach
mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
"""


mybooks = [
    {"Title": "Android App Development", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "25000", "Published_Year": "2017"},
    {"Title": "Python", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
    {"Title": "JavaScript", "Author": "Pham Dieu",
     "Publisher": "SSS", "Price": "38000", "Published_Year": "2018"},
    {"Title": "HTML5", "Author": "Man Nhi",
     "Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
    {"Title": "Compiler", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "24000", "Published_Year": "2011"},
    {"Title": "C language", "Author": "Man Nhi",
     "Publisher": "SSS", "Price": "29000", "Published_Year": "2010"},
    {"Title": "Programming Linguistics", "Author": "Pham Dieu",
     "Publisher": "HCM", "Price": "41000", "Published_Year": "2009"},
    {"Title": "C# language", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "42000", "Published_Year": "2013"},
    {"Title": "App Inventor", "Author": "Man Nhi",
     "Publisher": "LD", "Price": "30000", "Published_Year": "2015"},
]

status = True
while status == True:
    check = False
    while check == False:
        select = input("""Select to search:
        1. Title
        2. Author
        3. Publisher
        select (1,2,3)
        """)

        if select == '1':
            kw = 'Title'
            break
        elif select == '2':
            kw = 'Author'
            break
        elif select == '3':
            kw = 'Publisher'
            break
        else:
            print('Invalid select, please select (1,2,3)')


    inputkw = input("Enter keyword to search: ")
    count = 0
    for row in mybooks:
        if inputkw == (row[kw]):
            count+=1
            print("Title: ", row["Title"])
            print("Author: ", row["Author"])
            print("Publisher: ", row["Publisher"])
            print("Price: ", row["Price"])
            print("="*50)
    if count == 0:
        print("Not Found")
    print("You have continued? (Y/N)")
    input_status = input()
    if input_status == "Y":
        status = True
    else:
        status = False
        
