myList = [1,4,5,"Hi",10,"Hello India","America",3,8,"!@3abc","*1!@#",11,"Hi"]
##
####new_list = re.findall(regex,myList)
##print(new_list)

#1. Write a function to get sum of all integers


def sum_integers():
    a_sum = 0
    for i in myList:
        if type(i) == int:
            a_sum += i
    print (a_sum)
sum_integers()



#####2. write a function to concatenate all characters

ans = []
for i in myList:
    ans = ans+' '+i
print(ans)
##

###3. write a function to return all non-digits and counts of non-digits


a = []
for i in myList:
    if type(i) != int:
        a.append(i)
        print(a)
        print(len(a))
        

    
###4. write a function to return list of alphabets and integer

for i in myList:
    if i is isalnum():
        print(i)



###5. write a function to return list of special character strings


        
###6. Write a function to return list of strings
##
##a = []
##for i in myList:
##    if type(i) == str:
##        a += i  
##print(a)
##

    



#7. Write a function to get characters where length is more than 5
