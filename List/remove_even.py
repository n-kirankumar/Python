#remove even numberes



a = [1,2,3,4,5,6]

b = [i for i in a if i%2 != 0]
print(b)
