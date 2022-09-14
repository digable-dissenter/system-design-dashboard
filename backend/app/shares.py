import pandas as pd
from app import main
from flask import request
from flask_cors import CORS
import json
from app.dataframes import df_EOD_Equity_Data, df_Index_Constituents, df_FTSEJSE_Index_Series, df_Industry_Classification_Benchmark, df_BA_Beta_Output

app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route("/api/shares/available-shares", methods=["GET"])
def getAvailableShares():
    shares_ls = df_Index_Constituents.Alpha.unique().tolist()
    
    results_dict = {}
    results_dict = {k:v for (k, v) in enumerate(shares_ls)}
    
    resp = json.dumps(results_dict)
    
    return resp

@app.route("/api/shares/share-prices", methods=['GET'])
def getSharePrice():
    qry = request.args
    instr = qry.get("instr")
    no_results = qry.get("no_results")

    equity_data_srt = df_EOD_Equity_Data.set_index(['Instrument','Date']).sort_index(level=["Date"], ascending=[False])
    equity_index_sub_df = equity_data_srt.loc[[instr]]
    equity_index_sub_df.reset_index(inplace=True)
    
    results_df = equity_index_sub_df.loc[:, ['Date', 'Price']]
    results_df['Date'] = results_df['Date'].dt.strftime('%Y-%m-%d')

    resp = results_df.head(no_results).to_json()
    
    return resp
