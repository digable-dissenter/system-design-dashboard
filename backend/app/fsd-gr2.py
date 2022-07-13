# imports for SQL data part
import pyodbc 
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy.engine import URL, create_engine, Inspector

# Use your own server connection here
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DAIYAAN;"
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


"""Keys in frames_dict Dictionary:
tbl_Industry_Classification_Benchmark
tbl_FTSEJSE_Index_Series 
tbl_EOD_Equity_Data
tbl_EOD_Interest_Rate_Data
tbl_Beta_Output 
tbl_BA_Beta_Output
tbl_Index_Constituents """

# cursor = cnxn.cursor()

# # convert to format yyyy-mm-dd
# date = date.strftime("%Y-%m-%d")  


# # build up our query string
# query = ("SELECT * FROM dbo.tbl_EOD_Equity_Data "
#          f"WHERE [Date] = '{date}'")

# # execute the query and read to a dataframe in Python
# data = pd.read_sql(query, cnxn)

# print(data.head(26))

# # close the connection
# del cnxn
# cnxn.close()

# # make a few calculations
# mean_price = data['Price'].mean()
# std_price = data['Price'].std()

# # get max price and price details
# max_vals = data[['Instrument', 'Price']].sort_values(by=['Price'], ascending=False).iloc[0]

# # write an email message
# txt = (f"End of Day Equity data for period {date}"
#         f"Mean prices: {mean_price}n"
#         f"Standard deviation of prices: {std_price}n"
#         f"Highest price of {max_vals['Price']} "
#         f"received for {max_vals['Instrument']} instrument.")

# This is a Test - Daiyaan