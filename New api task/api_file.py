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

class KiranData(Base):
    __tablename__ = "kiran_data"
    Name = Column("name", String)
    Mob = Column("mob", Integer, primary_key=True)
    Age = Column("age", Integer)
    Gender= Column("gender", String)
    Error = Column("error", String)
    Is_new = Column("is_new", BOOLEAN)
#
@app.route('/insert_records', methods=['POST'])
def insertRecords():
    req_body = request.get_json(force=True)
    print("req_body is ---", req_body)
    print("enumerate(req_body)------",enumerate(req_body))
    for index, item in enumerate(req_body):
        record = KiranData(Name = item["name"],
                        Mob = item["mob"],
                        Age = item["age"],
                        Gender = item["gender"],
                        Error =  item ["error"],
                        Is_new = item["is_new"])
    session.add_all([record])
    session.commit()
    return ("data inserted")
@app.route('/get_all_records', methods=['GET'])
def home():
    result = session.query(KiranData).all()
    result = [item.__dict__ for item in result]
    return str(result)


# @app.route('/multi_record', methods=['GET'])
# def get_multi_record():
#     var4 = request.args.get('email')
#     var5 = request.args.get('password')
#     result = session.query(KiranData).filter(or_(KiranData.Email == var4, KiranData.Password == var5)).all()
#     result = [item.__dict__ for item in result]
#     return str(result)

app.run(debug=False)

