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

class Table3(Base):
    __tablename__ = "table3"
    Name = Column("name", String)
    Mob = Column("mob", String, primary_key=True)
    Email = Column("email", String)
    Full_addr = Column("full_addr", String)


@app.route('/printtable3', methods=['GET'])
def home():

    result = session.query(Table3).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)

app.run(debug=False)
"""

@app.route('/printtable2singlerecord', methods=['GET'])
def getSingleRecord():
    # http://127.0.0.1:5000/printtable2singlerecord?mobile=1234
    var1 = request.args.get('mobileNO')
    # select * from table where mobile==1234
    result = session.query(Table2).filter(Table2.Mob==var1).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)

@app.route('/table2selectedrecord', methods=['GET'])
def getMultipleRecord():
    # http://127.0.0.1:5000/table2selectedrecord?mobileNo=1234,5647
    var2 = [int(numbers) for numbers in request.args.get('mobileNo').split(",")]
    result = session.query(Table2).filter(Table2.Mob.in_(var2)).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)

@app.route('/table2startswithrecord', methods=['GET'])
def getStartsRecord():
    # http://127.0.0.1:5000/table2startswithrecord?name=kir
    var3 = request.args.get('name')
    # 'Joh%' - Matches with Johnson John Hohnavi...
    result = session.query(Table2).filter(Table2.Name.like(var3+'%')).all() # 'kiran'+'%' --> "kiran%"
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)

@app.route('/table2multifetchrecord', methods=['GET'])
def getMultiFetchRecord():
    # http://127.0.0.1:5000/table2multifetchrecord?name=kiran&mobile=1234
    var4 = request.args.get('name')
    var5 = request.args.get('mobile')
    result = session.query(Table2).filter(or_(Table2.Name==var4,Table2.Mob==var5)).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)



app.run(debug=False)
"""
