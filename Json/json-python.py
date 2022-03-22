#Write a Python program to convert JSON data to Python object.


import json
json_obj =  '{ "Name":"kiran", "Class":"xvii", "Age":50 }'

print("json input is --->>>> {} .".format(json_obj))


dict_obj = json.loads(json_obj)
print("python dict out put is ------>>>>> {} ".format(dict_obj))