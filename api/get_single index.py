from flask import Flask ,jsonify
app =Flask(__name__)


student_info = [{"name":"kiran1","age":27},{"name":"kiran2","age":29},{"name":"kiran3","age":28}]



@app.route('/kiran')
def index():
    return"Hi Kiran"


@app.route("/records",methods = ["GET"])
def get():
    return jsonify({"details":student_info})



@app.route("/single_records/<int:"age">",methods = ["GET"])
def get_age():
    return jsonify({"Details":student_info[iage]})



if __name__=="__main__":
    app.run(debug=False)
