from math import sqrt
q= ["2 + 5 + 7 =","5 * 10 =", "sqrt(16) =", "12 % 2 =", "5 // 2 ="]

for i in q:
    kq = eval(i.strip("="))
    
    ip = float(input(i))
    while ip!= kq:
        print("Incorrect answer!")
        ip = float(input(i))
    else:
        print("Correct answer")
