import re
myStr = "Russian president is Vladimir Putin and his password is 1234@#$%"

a = re.findall("[A-Za-z]",myStr)
b = re.findall("[0-9]",myStr)
c = re.findall("[^a-zA-Z0-9]",myStr)

a1="".join(a)
b1 = "".join(b)
c1 = "".join(c)

myDict = {"num" : b1, "alpha" : a1,  "special" : c1}

print(myDict)
