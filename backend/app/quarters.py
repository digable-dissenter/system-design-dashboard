import pandas as pd
from app import main
from flask import request, Response
from flask_cors import CORS, cross_origin
from app.dataframes import df_Index_Constituents

app = main.app
CORS(app, resources={r"/*":{'origins':"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/quarters")
@cross_origin()
def getDates():
    results_df = df_Index_Constituents['Date'].unique()    
    
    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp