
import json
import psycopg2
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os
app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

class SignUp(Base):
    __tablename__ = "signup"
    firstName=Column ("first_name",String)
    lastName=Column("last_name",String)
    email=Column("email",String,primary_key=True)
    password=Column("password",String)
   
@app.route('/get_all_records', methods=['GET'])
def home():
    result = session.query(SignUp).all()
    result = [item.__dict__ for item in result]
    return str(result)


@app.route('/multi_record', methods=['GET'])
def getMultiRecord():
    var4 = request.args.get('email')
    var5 = request.args.get('password')
    result = session.query(SignUp).filter(and_(SignUp.email==var4,SignUp.password==var5)).all()
    result = [item.__dict__ for item in result]
    if result:
        return str(result)
    else:
        return "invalid details.Please enter correct username and password"


@app.route('/update_records',methods=['PATCH'])
def update_record():
    Email = request.args.get('email')
    Password = request.args.get('password') 
    result=session.query(SignUp).filter(SignUp.email==Email).update({"password":Password})
    session.commit()
    return ("data updated")

#http://127.0.0.1:5000/update_records?email=a6@gmail.com6&password=kiran7_a7


@app.route('/delete_records',methods=['DELETE'])
def delete_record():
    Email = request.args.get('email')
    result=session.query(SignUp).filter(SignUp.email==Email).delete()
    if result:
        session.commit()
        return ("record removed succesfully")
    else:
        return "enter the correct field"

@app.route('/remove_records',methods=['DELETE'])
def remove_record():
    Email = request.args.get('email')
    for i in Email:
        if i:
            result=session.query(SignUp).filter(SignUp.email==Email).delete()
            if result:
                session.commit()
                return ("record removed succesfully")
            else:
                return "enter the correct field"





@app.route('/sign_up', methods=['POST'])
def insertRecords():
    record = []
    response_message = []
    req_body = request.get_json(force=True)
    for item in req_body:
        if "first_name" in item and "email" in  item and 'password' in item and 'last_name' in item:
            user_details = session.query(SignUp).filter(SignUp.email==item.get("email")).all()
            if user_details:
                return"user is already registered"
            else:
                record = SignUp(firstName = item["first_name"],
                                lastName = item["last_name"],
                                email = item["email"],
                                password = item["password"])
        else:
            response_message.append("first_name,lastname, email and pasword - mandatory fields")
    
    if response_message:
        return str(response_message)
    else:
        session.add_all([record])
        session.commit()
        return "Data has been inserted successfully"
app.run(debug=False)



