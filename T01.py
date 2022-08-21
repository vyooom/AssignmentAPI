from flask import Flask, request, jsonify
import mysql.connector as mysql
import pandas as pd

db = mysql.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894')

cursor = db.cursor()
# database api_db
cursor.execute('create database if not exists api_db')
q1 = 'create table if not exists api_db.entry(id int(4), name varchar(20), surname varchar(20), age int(3))'
cursor.execute(q1)

db.commit()
# T01. Write a program to insert a record in sql table via api

app = Flask(__name__)

@app.route('/T01', methods = ['GET', 'POST'])
def insertRecord():
    if(request.method == 'POST'):
        a = request.json['id']
        b = request.json['name']
        c = request.json['surname']
        d = request.json['age']
        data = (a,b,c,d)
        q2 = 'insert into api_db.entry values(%s, %s, %s, %s)'
        cursor.execute(q2, data)
        db.commit()


if __name__ == '__main__':
    app.run()