a = {6,7,8,9,10}
b ={5,6,7,8,9}
a.add(4)
b.add(3)
c=a.union(b)
print(c)
d=a.difference(b)
print(d)
e=a.intersection(b)
print(e)

lst = [11, 100, 99, 1000, 999, 99]
print(lst[1])
print(lst[-1])
x=lst.count(99)
print(x)
for a in lst:
    n=0
    a+=n
print(a)   

y = range[2020 , 2070]
for a in y:
    if a % 5 == 0:
        print(y)

z = range[1000 , 2000]
for b in z:
    if b/7 == 0 && b%5 !=0:
        print(b)
