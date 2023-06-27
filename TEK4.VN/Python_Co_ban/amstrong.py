
while True:
  n = int(input())
  num =n
  s =0
  k = len(str(n))
  while num !=0:
    res = num%10
    s +=res**k
    num=num//10
  if s == n:
    print(n,"is an Armstrong number")
    break
    