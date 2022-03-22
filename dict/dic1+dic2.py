
def add_dict():
        
    a = {1:10,2:20}
    b = {3:30,4:40}
    c = {}
    for i in (a,b):
        c.update(i)
    print(c)
add_dict()
