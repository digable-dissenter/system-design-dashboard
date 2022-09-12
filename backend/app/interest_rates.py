import pandas as pd
from app import main
from flask import jsonify, request
from app.dataframes import df_EOD_Interest_Rate_Data

app = main.app

@app.route('/api/int-rates/')
def getIntRates():
    qry_args = request.args
    curve = qry_args.get("curve")
    tenor = qry_args.get("tenor")
    # Divide Rate by 100, round to 2 decimal places, and convert to JSON
    qry = 'Tenor == {0} and Curve >= {1}'.format(tenor, curve)
    results_df = df_EOD_Interest_Rate_Data.query(qry, inplace = True)

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp

@app.route('/api/int-rates/dates/')
def getIntRateDates():
    # Order by Date, then Convert to JSON - numpy values are not JSON serializable
    results_df = df_EOD_Interest_Rate_Data['Date'].unique()  

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp

@app.route('/api/int-rates/dates/')
def getYC():    
    qry_args = request.args
    date = qry_args.get("date")
    tenor = qry_args.get("tenor")
    
    qry = 'Tenor == {0} and Date = {1}'.format(tenor, date)
    # Divide Rate by 100, round to 2 decimal places, and convert to JSON (Order by Tenor)
    results_df = df_EOD_Interest_Rate_Data.query(qry, inplace = True)

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp