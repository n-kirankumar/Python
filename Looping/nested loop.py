sampleDict = dict([('first', 1),('second', 2),('third', 3)])
print(sampleDict)


dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)


for l in 'kiran':
   if l == 'a':
      pass
   print(l)


   
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break



var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)


##
##for i in range(10):
##    for j in range(11,21):
##        print(i, j)





