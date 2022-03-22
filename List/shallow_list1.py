
import iterables

a = [10,[20,30],[40,50,60],70]

b= []
c = []
for i in a:
    if type(i) == list:
        b.append(i)
    elif type(i) != list:
        c.append(i)

print(b)
print(c)



print(d)
