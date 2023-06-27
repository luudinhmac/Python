# Counter
from collections import Counter
c = Counter("Hello world")
#print(c)
print(c.most_common(4))
#print(Counter(['1', '2','3', '4']))
print(c['l'])
c2 = Counter(coca = 5, pepsi =10)
#print(list(c2.elements()))
d = ['a','b', 'a', 'e']
c3= Counter(a=3, b=5, c=7, e=-5,d=-2)
c3.subtract(d)
#print(c3)