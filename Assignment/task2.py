import re
myStr = "Russian president is Vladimir Putin and his password is !@#$%^&125444"
myList = []

def count_each_character():
    myDict = {}
    for i in myStr:
        myDict[i] = myStr.count(i)
    return myDict
count_each_character()


def alpha_numbers_special():
    dict1 = {"alphabets":"".join(re.findall("[A-Za-z]",myStr)),"numbers":"".join(re.findall("[0-9]",myStr)),"special":"".join(re.findall("[^a-zA-Z0-9]",myStr))}
    print(dict1)
alpha_numbers_special()


def seperate_alpha_numbers_special():
    my_dict1 = {"alphabets":None,"numbers":None,"special":None}
    number_count = 0
    alphabets_count = 0
    special_count = 0
    for i in myStr:
        if i.isalpha():
            alphabets_count += 1
        elif i.isdigit():
            number_count += 1
        else:
            special_count += 1
    my_dict1["alphabets"] = alphabets_count
    my_dict1["numbers"] = number_count
    my_dict1["special"] = special_count
    return my_dict1
seperate_alpha_numbers_special()


# print(seperate_alpha_numbers_special(),count_each_character(),alpha_numbers_special())








