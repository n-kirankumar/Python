import json

python_obj = {
  "name": "kiran",
  "class":"I",
  "age": 6
}
print(type(python_obj))


# convert into JSON:
jason_data = json.dumps(python_obj)

# result is a JSON string:
print(jason_data)

print(type(jason_data))