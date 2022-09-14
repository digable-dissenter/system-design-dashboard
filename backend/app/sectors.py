import pandas as pd
from app import main
import json
from flask import jsonify, request, Response
from flask_cors import CORS
from app.dataframes import df_Index_Constituents, df_Industry_Classification_Benchmark, df_BA_Beta_Output

app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route("/api/sectors/available-sectors", methods=["GET"])
def getAvailableSectors():
    sectors_ls = df_Industry_Classification_Benchmark.Sector.unique().tolist()
    
    results_dict = {}
    results_dict = {k:v for (k, v) in enumerate(sectors_ls)}
    
    resp = json.dumps(results_dict)
    
    return resp
