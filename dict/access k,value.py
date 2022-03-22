
def access_key_value():
    
    a = {1:10,2:20,1:30}
    keys = []
    values = []
    key_values = []
    
    for i in a.keys():
        keys.append(i)
    print("keys : ",keys)
    for i in a.values():
        values.append(i)
    print("values : ",values)
    for i,j in a.items():
        print(i,j)
access_key_value()
