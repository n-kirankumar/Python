import json

p = '{"name": "Bob", "languages": ["Python", "Java"]}'
q = json.loads(p)
print(type(q))
#
# person_dict = {"name": "Bob",
# "age": 12,
# "children": None
# }
# print(person_dict)
# person_json = json.dumps(person_dict)
#
#
# print(person_json)
# Output: {"name": "Bob", "age": 12, "children": null}
# print(type(person_json))

