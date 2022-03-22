a = [10,20,30,20,10,50,60,40,80,50,40]

b = set()
c = []
for i in a:
    if i not in b:
        c.append(i)
        b.add(i)
print(b)




##a = [10,20,30,20,10,50,60,40,80,50,40]
##
##dup_items = set()
##uniq_items = []
##for x in a:
##    if x not in dup_items:
##        uniq_items.append(x)
##        dup_items.add(x)
##
##print(dup_items)
