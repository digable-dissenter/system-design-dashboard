# imports for SQL data part
# import pyodbc 
import pandas as pd
from sqlalchemy.engine import URL, create_engine

# Use your own server connection here
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N5Q4FJ2;"
            "Database=AIFMRM_ERS;"
            "Trusted_Connection=yes;")

cnxn_url = URL.create("mssql+pyodbc", query={"odbc_connect": cnxn_str})

engine = create_engine(cnxn_url)

# initialise connection via context manager           
with engine.connect() as cnxn:
        tables_df = pd.read_sql('SELECT [name] AS [table_name] FROM sys.tables', cnxn)
        table_name_list = tables_df.table_name
        select_template = 'SELECT * FROM {table_name}'
        # Dictionary of table names and their respective SQL queries
        frames_dict = {}
        for tname in table_name_list:
                query = select_template.format(table_name = tname)
                frames_dict[tname] = pd.read_sql(query, cnxn)

print(frames_dict)