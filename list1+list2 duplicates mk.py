a = [1, 2, 3, 4, 5, 6, 7, 12, 13]
b = [4, 5, 6, 7, 8, 9, 1, 2]
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)
print("common elements in both lists are :", c)