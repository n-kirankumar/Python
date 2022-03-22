import functools
test = (lambda x: functools.reduce(int.__mul__, range(1,x+1),1))(2)
print(test)