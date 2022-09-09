from flask import Flask
from flask_cors import CORS, cross_origin
from sqlalchemy.engine import create_engine
import pandas as pd
import pyodbc
from app.db import DatabaseClient

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"

db_client = DatabaseClient()

cnxn = db_client.pyodbc_localhost()

engine = create_engine(cnxn)
class Database_df:
    def __init__(self, tables_df=pd.DataFrame(), table_name_list=[], select_template='', frames_dict={}):
        self.tables_df = tables_df
        self.table_name_list = table_name_list
        self.select_template = select_template
        self.frames_dict = frames_dict

    def create_dataframes(self, engine):
        # initialise connection via context manager           
        with engine.connect() as cnxn:
            self.tables_df = pd.read_sql('SELECT [name] AS [table_name] FROM sys.tables', cnxn)
            self.table_name_list = self.tables_df.table_name
            self.select_template = 'SELECT * FROM {table_name}'
            # Dictionary of table names and their respective SQL queries
            self.frames_dict = {}
            for tname in self.table_name_list:
                query = self.select_template.format(table_name = tname)
                self.frames_dict[tname] = pd.read_sql(query, cnxn)
            # Close db connection
            cnxn.close()
            # Return dictionary of dataframes
            return self.frames_dict

frames_dict = Database_df().create_dataframes(engine)