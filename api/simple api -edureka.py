from flask import Flask ,jsonify
app =Flask(__name__)


courses = [{"name":"kiran","age":"27"},{"name":"kiran2","age":"29"},{"name":"kiran3","age":"28"}]



@app.route('/kiran')
def index():
    return"Hi Kiran"


@app.route("/records",methods = ["GET"])
def get():
    return jsonify({"cssourses":courses})

if __name__=="__main__":
    app.run(debug=False)
