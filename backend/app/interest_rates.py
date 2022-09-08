import pandas as pd
from app import main
from flask import jsonify, request, Response
from flask_cors import CORS
from app.dataframes import df_EOD_Interest_Rate_Data

app = main.app
CORS(app, resources={r"/*":{'origins':"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/int-rates/')
@cross_origin()
def getIntRates():
    qry_args = request.args
    curve = qry_args.get("curve")
    tenor = qry_args.get("tenor")

    # Divide Rate by 100, round to 2 decimal places, and convert to JSON
    qry = 'Tenor == {0} and Curve >= {1}'.format(tenor, curve)
    results_df = df_EOD_Interest_Rate_Data.query(qry, inplace = True)

@app.route('/api/int-rates/dates/')
@cross_origin()
def getIntRateDates():

    # Order by Date, then Convert to JSON
    results_df = df_EOD_Interest_Rate_Data['Date'].unique()  

@app.route('/api/int-rates/dates/')
@cross_origin()
def getYC():    
    qry_args = request.args
    date = qry_args.get("date")
    tenor = qry_args.get("tenor")
    
    qry = 'Tenor == {0} and Date = {1}'.format(tenor, date)
    # Divide Rate by 100, round to 2 decimal places, and convert to JSON (Order by Tenor)
    results_df = df_EOD_Interest_Rate_Data.query(qry, inplace = True)