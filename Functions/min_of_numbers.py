def find_min_of_numbers():
    my_list = [1,2,3,4,-5]
    min = my_list[0]
    for i in my_list:
        if i <= min:
            min=i
    print(min)
find_min_of_numbers()


