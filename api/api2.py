import json
import psycopg2
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
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


class GlobalLogicEmployee(Base):
    __tablename__ = "gl_employee"
    firstName = Column("first_name", String)
    lastName = Column("last_name", String)
    age = Column("age", Integer)
    mobileNumber = Column("mobile_number", Integer, primary_key=True)
    emailId = Column("email_id", String)
    dob = Column("dob", String)
    isOld = Column("is_old", BOOLEAN)


@app.route('/insert_data', methods=['POST'])
def insert_records():
    record = []
    error_container = []
    req_body = request.get_json(force=True)
    print(req_body)
    for dict_item in req_body:
        if "first_name" in dict_item and "email_id" in dict_item:
            if dict_item.get("first_name") != str and len(dict_item.get("first_name")) <= 50:
                pass
            else:
                error_container.append("max allowed characters are 50 but {} are given".format(len(dict_item.get("first_name"))))

            if dict_item.get("last_name") != str and len(dict_item.get("last_name")) <= 50:
                pass
            else:

                error_container.append("max allowed characters are 50 but {} are given".format(len(dict_item.get("last_name"))))

            if dict_item.get("age") == int:
                pass
            else:
                error_container.append("You have entered incorrect age")

            if dict_item.get("mobile_number") == int :
                pass
            else:
                error_container.append("You have entered incorrect mob num")

            if dict_item.get("email_id") == str and len(dict_item.get("email_id")) <= 30:
                pass
            else:
                error_container.append("max email id is 30 but {} is given ".format((len(dict_item.get("email_id")))))

            if dict_item.get("dob") == str and len(dict_item.get("dob")) <= 20:
                pass
            else:
                error_container.append("max dob is 20 but {} is given ".format((len(dict_item.get("dob")))))
            print('ERROR is {}'.format(error_container))
            # if dict_item.get("isOld") == BOOLEAN:
            #     pass
            # else:
            #     error_container.append("only boolean records are allowed but you have giv is given ")
        else:
            return"first_name and email are mandatory fields"

    if error_container:
        return {"message": error_container, "status": "Failed"}
    else:
        record = GlobalLogicEmployee(firstName=dict_item["first_name"],
                                    lastName=dict_item["last_name"],
                                     age=dict_item["age"],
                                     mobileNumber=dict_item["mobile_number"],
                                     emailId=dict_item["email_id"],
                                     dob=dict_item["dob"],
                                     isOld=dict_item["is_old"])
        session.add_all([record])
        session.commit()
        return {"msg": "Data has been inserted successfully"}


@app.route('/get_all_records', methods=['GET'])
def home():
    result = session.query(GlobalLogicEmployee).all()
    result = [item.__dict__ for item in result]
    return str(result)


@app.route('/multi_record', methods=['GET'])
def get_multi_record():
    var4 = request.args.get('email')
    var5 = request.args.get('password')
    result = session.query(GlobalLogicEmployee).filter(or_(GlobalLogicEmployee.Email == var4, GlobalLogicEmployee.Password == var5)).all()
    result = [item.__dict__ for item in result]
    return str(result)

app.run(debug=False)

