
#Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

##dic1={1:10, 2:20}
##dic2={3:30, 4:40}
##dic3={5:50,6:60}
##
##
##dic ={}
##for i in (dic1,dic2,dic3):
##    dic.update(i)
##print (dic)



    

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)




sum1 = []
for i in dic1.values():
    print(i)
    sum1.append(i)
print(sum1)
   

