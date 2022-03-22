#shallow list



import itertools

a = [[1,2,3],[4,5,6],[7],[8,9,10]]

b = list(itertools.chain.from_iterable(a))
print(b)




c = [[1,2,3],[4,5],["kiran"],["hello","sad"]]

d =list(itertools.chain.from_iterable(c))
print(d)
