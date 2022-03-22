a =[{'first_name': 'kiran3', 'last_name': 'n3', 'age': 25, 'mobile_number': 9, 'email_id': 'kiran4@gmail.com', 'dob': '04-04-2020', 'is_old': 'False'}]

print(type(a))



for req_body in a:
    a = req_body.get("first_name")
    print (a)
    print(len(a))
    print(type("a"))
    print("a" == str)

    if req_body.get("first_name") and req_body.get("mobile_number"):
        if req_body.get("first_name") == str:
            pass
        else:
            print("name")

    else:
        print("first_name and mobile_number is mandatory field")


