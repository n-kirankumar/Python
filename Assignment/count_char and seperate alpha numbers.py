import re
myStr = "Russian president is Vladimir Putin and his password is !@#$%^&125444"
myList = []
countDict = {}
for i in myStr:
    countDict[i] = myStr.count(i)
alpha_join = "".join(re.findall("[A-Za-z]",myStr))
number_join = "".join(re.findall("[0-9]",myStr))
special_join = "".join(re.findall("[^a-zA-Z0-9]",myStr))
sepDict = {"alphabets":alpha_join,"numbers":number_join,"special":special_join}
myList.append(countDict)
myList.append(sepDict)
print(myList)
print(myList[1]['alphabets'])









