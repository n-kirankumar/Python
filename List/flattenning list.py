a = [[1,2,3],[4,5,6],[7,8,9]]
##b = []
##for i in a :
##    for j in i:
##        b.append(j)
##print(b)


b =[i for i in a and j for j in i]
print(b)
