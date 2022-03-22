##Fill a list with a sequence of numbers:



new_list = [i for i in range(5)]
print(new_list)



#printing squares

a = [x**2 for x in range(5)]
print(a)

#Printing cubes

b = [x**3 for x in range(5)]
print(b)


#Giving filter conditions by using if

c = [i for i in range(20) if i%2 == 0]
print(c)
