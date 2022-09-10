import pandas as pd
from app import main
from flask import request, Response
from app.dataframes import df_Index_Constituents

app = main.app

@app.route("/api/quarters")
def getDates():
    results_df = df_Index_Constituents['Date'].unique()    
    
    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp