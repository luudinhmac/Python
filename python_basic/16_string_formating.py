# string formatting 
# %, .format(), -f string

my_string = "Toi la Luu Dinh Mac"
age = 28 
money = 10.0123
print("Xin chao cac ban! {}, {} tuoi, co {:.2f} VND ".format(my_string,age,money))
print("Xin chao cac ban! %s, %i tuoi, co %.2f VND " %(my_string,age,money)
)
print(f"Xin chao cac ban! {my_string}, {age} tuoi, co {money:.2f} VND ".format(my_string,age,money)
)