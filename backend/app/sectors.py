import pandas as pd
from app import main
from flask import jsonify, request, Response
from flask_cors import CORS, cross_origin
from app.dataframes import df_Index_Constituents, df_Industry_Classification_Benchmark, df_BA_Beta_Output

app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route("/api/sectors/available-sectors")
@cross_origin()
def getAvailableSectors():
    results_df = df_Industry_Classification_Benchmark.drop_duplicates()
    
    return results_df.to_json(orient='records')
    # resp = jsonify(results_df)

    # resp.status_code = 200

    # return resp
