string=input()

ol = [i for i in string.split() if len(i) < 5]
print(ol)