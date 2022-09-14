import pandas as pd
from app import main
from flask import request, Response
from flask_cors import CORS
from app.dataframes import df_Index_Constituents
import json

app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route("/api/quarters", methods=["GET"])
def getDates():
    dates_ls = df_Index_Constituents.Date.dt.strftime('%Y-%m-%d').unique().tolist()
    results_dict = {}
    results_dict = {k:v for (k, v) in enumerate(dates_ls)}
    
    resp = json.dumps(results_dict)
    
    return resp