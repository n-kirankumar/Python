def count_alpha_number_special():
    """"function to count alphabets numbers and special
    chars in the string"""
    myStr="Russian president is Vladimir Putin and his password is 1234@#$%"
    myDict = {"num":None,"alpha":None,"special":None}
    # initialise starting count as zero
    number = 0
    alpha = 0
    special = 0
    for i in myStr:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            number += 1
        else:
            special += 1

    myDict["num"] = str(number)
    myDict["alpha"] = str(alpha)
    myDict["special"] = str(special)
    print(myDict)
count_alpha_number_special()











