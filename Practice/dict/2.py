# tach so va chu rieng
# CHUYEN DOI  str1 sang dang so

dic = {
    "A": 1, "B": 2, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2,
    "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1,
    "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1,
    "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}
str_1 = "University of Technology and Education"
num = []
alpha = []
for i in dic:
    num.append(str(dic[i]))
    alpha.append(i)

num1 = " ".join(num)
alpha1 = " ".join(alpha)
print(num1)
print(alpha1)
sum = 0
for j in dic:
    sum += dic[j]
print(sum)

str_1 = str_1.upper()
print(str_1)
str2 = ""
for k in str_1:
    if k == " ":
        str2 =str2+ k
    else:
        str2 = str2 + str(dic[k])

print(str2)