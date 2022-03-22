from flask import Flask,request
app = Flask(__name__)




@app.route("/sign_in",methods=['GET'])
def get_data():
    a = {"kiran":"1234","kiran2":"5678"}
    user_name = request.args.get("name")
    password = request.args.get("password")
    if user_name in a and password in a[user_name]:
        return"succesful login"
    else:
        return"invalid credentials"
app.run(debug=False)
