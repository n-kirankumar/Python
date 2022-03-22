
list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

def merge_list():
    new_list =[]
    for i in list_1:
        if i%2 != 0:
            new_list.append(i)
    for i in list_2:
        if i%2 == 0:
            new_list.append(i)
    print(new_list)
    
merge_list()

