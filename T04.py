from flask import Flask, request, jsonify
import mysql.connector as mysql
import pandas as pd

db = mysql.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'api_db')

cursor = db.cursor()

# T04. Write a program to fetch a record via api

app = Flask(__name__)

@app.route('/T04', methods = ['GET', 'POST'])
def fetchRecord():
    if(request.method == 'POST'):
        df = pd.read_sql('select * from api_db.entry', db)
        df = pd.DataFrame(df)
        df = df.to_json()
        return jsonify(df)


if __name__ == '__main__':
    app.run()