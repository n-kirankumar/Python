a = "KiKKKRaNkjdhherrhbGHJMhdkd"


b = []
for i in a:
    if i.isupper():

        
        b.append(a.index(i))
        for i in b:
            if i == a[i]:
                b.append(a.index(i))
print(b)

