from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import json
import random
import os
# import psycopg2

app = Flask(__name__)

db  = SQLAlchemy(app)
db_cred = {
    'user': 'postgres',         # DATABASE USER
    'pass': 'postgres',     # DATABASE PASSWORD
    'host': '127.0.0.1',    # DATABASE HOSTNAME
    'name': 'db'   # DATABASE NAME
}
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://\
{db_cred['user']}:{db_cred['pass']}@{db_cred['host']}/\
{db_cred['name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
#Executing an MYSQL function using the execute() method
@app.route('/api/week5/',methods=[ 'GET'])
def week5():
    select_stmt = "SELECT foodname, price FROM food ORDER BY random() LIMIT 1"

    foodmenu=db.engine.execute(select_stmt)

    for record in foodmenu:
        return record
    # try:
    #     cursor.execute(select_stmt)
    # except Exception as e:
    #     print(e.message)
    #     conn = psycopg2.connect( 
    # database = os.environ.get('POSTGRES_DB'), 
    # user = os.environ.get('POSTGRES_USER'),
    # password = os.environ.get('POSTGRES_PASSWORD'),
    # host = os.environ.get('DB_HOST'),
    # port = os.environ.get('DB_PORT')
    # )

    # cursor = conn.cursor()
    # res =list(cursor.fetchone())
    # cursor.close()
    # conn.close()
    # return jsonify({"We recommend": res[0],"price": res[1]})




