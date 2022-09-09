
import pyodbc
class DatabaseClient:
    def __init__(self):
        self.pyodbc_localhost()

    def pyodbc_localhost(self):
        driver = '/usr/lib/libtdsodbc.so'
        server = "localhost"
        database = "AIFMRM_ERS"
        username = 'sa'
        password = 'Ritravatra00043)'
        port = '1433'
        try:
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}')
        except Exception as e:
            print(f"Couldn't connect to db on localhost because {e}")
        else:
            self.cursor = cnxn.cursor()
            return cnxn


db_client = DatabaseClient()
db_client.pyodbc_localhost()
