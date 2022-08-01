from app import main
from flask import request, render_template, Response
from flask_cors import CORS
from app import weights_and_ics
from app import betas_mkt_spec_vols
from app import calc_stats
import json

app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
@app.route('/home')
def home_page():
    return("Shark🦈!")

@app.route('/weights_and_ics', methods=['GET'])
def weights():
    res = weights_and_ics.getICsAndWeights("2020-01-01","ALSI","tbl_Index_Constituents")
    # weights_ = []

    # for i in res:
    #     weights_.append({'Alpha':i['Alpha'],'Weights':i['Weights']})
    
    return res.to_json(orient='records') # Response(json.dumps(weights_), mimetype='application/json')

@app.route('/betas_mkt_spec_vols', methods=['GET'])
def volatilities():
    ICs = weights_and_ics.getICsAndWeights("2020-01-01","ALSI","tbl_Index_Constituents")
    ICs = ICs['Alpha']
    res = betas_mkt_spec_vols.getBetasMktAndSpecVols("2020-01-01",ICs,"tbl_BA_Beta_Output","J203")
    # weights_ = []

    # for i in res:
    #     weights_.append({'Alpha':i['Alpha'],'Weights':i['Weights']})
    
    return res.to_json(orient='records') # Response(json.dumps(weights_), mimetype='application/json')

@app.route('/stats', methods=['GET'])
def stats():
    ICs = weights_and_ics.getICsAndWeights("2020-01-01","ALSI","tbl_Index_Constituents")
    ICs = ICs['Alpha']
    res = calc_stats.getBetasMktAndSpecVols("2020-01-01",ICs,"tbl_BA_Beta_Output","J203")
    # weights_ = []

    # for i in res:
    #     weights_.append({'Alpha':i['Alpha'],'Weights':i['Weights']})
    
    return res.to_json(orient='records') # Response(json.dumps(weights_), mimetype='application/json')