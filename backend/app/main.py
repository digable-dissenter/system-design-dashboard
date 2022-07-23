from flask import Flask, render_template, request, jsonify, json
# from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL, create_engine, Inspector
import pandas as pd

app = Flask(__name__)

# Cors = CORS(app)

# CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS = True)

# app.config['CORS_HEADERS'] = 'Content-Type'

# Use your own server connection here
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N5Q4FJ2;"
            "Database=AIFMRM_ERS;"
            "Trusted_Connection=yes;")

cnxn_url = URL.create("mssql+pyodbc", query={"odbc_connect": cnxn_str})

# initialise connection via context manager           
with engine.connect() as cnxn:
    '''
        This context manager code is used to connect to the database, 
        retrieve the database tables, load the tables into a dictionary of pandas dataframes,
        and then close the database connection.
    '''
    tables_df = pd.read_sql('SELECT [name] AS [table_name] FROM sys.tables', cnxn)
    table_name_list = tables_df.table_name
    select_template = 'SELECT * FROM {table_name}'
    # Dictionary of table names and their respective SQL queries
    frames_dict = {}
    for tname in table_name_list:
        query = select_template.format(table_name = tname)
        frames_dict[tname] = pd.read_sql(query, cnxn)

    cnxn.close()