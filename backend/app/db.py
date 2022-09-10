
import pyodbc
class DatabaseClient:
    def __init__(self):
        self.pyodbc_localhost()

    def pyodbc_localhost(self):
        driver = '{ODBC Driver 17 for SQL Server}'
        server = "localhost"
        database = "AIFMRM_ERS"
        cnxn_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        try:
            cnxn = pyodbc.connect(cnxn_string)
        except Exception as e:
            print(f"Couldn't connect to db on localhost because {e}")
        else:
            self.cursor = cnxn.cursor()
            return cnxn_string
