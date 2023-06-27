# POSITIONAL , KEYWORDS ARGUMENT, *ARGS, **KWARGS 
# function
print("================== FUNCTION ========================")
def func(x,y,z):
    print(x,y,z)
# positional arguments
func (1,2,3)
# keyword arguments
func (y = 1,z = 2, x = 'keyword')

# *args  
# Truyen list cac tham so
# Là tham số không bắt buộc
print("========================= *args ====================================")
def funcs(x,y, *args):
    print(x,y)
    print(args)
    for x in args:
        print (x)

funcs(1,2, 123,'xin chao la chao xin', True)

# **keywargs : can pass any number of keyword arguments arguments to your function
print("========================== **keywargs==========================")
def func2(x,y,**kwargs):
    print (x,y)
    for x in kwargs.items():
        print(x)

func2(1,2, a =10, b =20, c ='Hello')