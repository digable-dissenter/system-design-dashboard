# from crypt import methods
import pandas as pd
from app import main
from flask import request
import json
from app.dataframes import df_EOD_Interest_Rate_Data

app = main.app

@app.route('/api/int-rates/', methods=['GET'])
def getIntRates():
    qry_args = request.args
    curve = qry_args.get("curve")
    tenor = qry_args.get("tenor")
    
    # Divide Rate by 100, round to 2 decimal places
    int_rates_df = df_EOD_Interest_Rate_Data.set_index(["Curve"])
    int_rates_df = int_rates_df.loc[[curve]]
    int_rates_df.reset_index(inplace=True)

    int_rates_df = int_rates_df.set_index(["Tenor"])
    int_rates_df = int_rates_df.loc[[tenor]]
    int_rates_df.reset_index(inplace=True)

    int_rates_df.set_index(['Date', 'Rate'])
    
    results_df = int_rates_df.loc[:, ['Date', 'Rate']]

    resp = results_df.to_json(orient='records') 
    
    return resp

@app.route('/api/int-rates/dates/', methods=['GET'])
def getIntRateDates():
    # Order by Date, then Convert to JSON - numpy values are not JSON serializable
    intdates_ls = df_EOD_Interest_Rate_Data.Date.dt.strftime('%Y-%m-%d').unique().tolist()
    
    results_dict = {}
    results_dict = {k:v for (k, v) in enumerate(intdates_ls)}

    resp = json.dumps(results_dict)
    
    return resp 
    
    

@app.route('/api/int-rates/yield/', methods=['GET'])
def getYC():    
    qry_args = request.args
    date = qry_args.get("date")
    curve = qry_args.get("curve")

    # Divide Rate by 100, round to 2 decimal places
    yc_df = df_EOD_Interest_Rate_Data.set_index(["Curve"])
    yc_df = yc_df.loc[[curve]]
    yc_df.reset_index(inplace=True)

    yc_df = yc_df.set_index(["Date"]).sort_index(level=["Date"], ascending=[False])
    yc_df = yc_df.loc[[date]]
    yc_df.reset_index(inplace=True)
    
    yc_df.set_index(['Tenor', 'Rate'])
    
    results_df = yc_df.loc[:, ['Tenor', 'Rate']]

    resp = results_df.to_json(orient='records') 
    
    return resp