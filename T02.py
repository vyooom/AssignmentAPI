from flask import Flask, request, jsonify
import mysql.connector as mysql
import pandas as pd

db = mysql.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'api_db')

cursor = db.cursor()
# T02.  Write a program to update a record via api

app = Flask(__name__)

@app.route('/T02', methods = ['GET', 'POST'])
def updateRecord():
    if(request.method == 'POST'):
        a = request.json['id']
        b = request.json['name']
        c = request.json['surname']
        d = request.json['age']
        data = (b,a)
        q = 'UPDATE api_db.entry SET name = %s where id = %s'
        cursor.execute(q, data)
        db.commit()
        return jsonify(str('Updation complete'))


if __name__ == '__main__':
    app.run()