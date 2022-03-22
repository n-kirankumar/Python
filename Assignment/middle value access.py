
def find_middle_character(a):
    b =""
    if len(a) %2 != 0:
        middle = len(a)//2
        print(a[middle])
    else:
        print("None")
find_middle_character("abcdef")