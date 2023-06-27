def div(a,b):
    try:
        c = (a+b)/(a-b)
    except Exception as err:
        print(err)
    else: 
        print(c)
    finally:
        print("This line always run")

div(2,2)


print(8//3)