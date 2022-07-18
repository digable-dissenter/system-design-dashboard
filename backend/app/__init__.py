from flask import Flask, render_template, request, jsonify, json
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL, create_engine, Inspector

app = Flask(__name__)

Cors = CORS(app)

CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS = True)

app.config['CORS_HEADERS'] = 'Content-Type'

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N5Q4FJ2;"
            "Database=AIFMRM_ERS;"
            "Trusted_Connection=yes;")

cnxn_url = URL.create("mssql+pyodbc", query={"odbc_connect": cnxn_str})

app.config['SQLALCHEMY_DATABASE_URI'] = 'cnxn_url'
db = SQLAlchemy(app)

@app.route("/dataentry", methods=["POST", "GET"])
def submitData():
    response_object = {'status':'success'}

    if request.method == "POST":
        post_data = request.get_json()
        name = post_data.get('name'),
        department = post_data.get('department')

        print(name)
        print(department)

        response_object['message'] = 'Data added!'

    return jsonify(response_object)