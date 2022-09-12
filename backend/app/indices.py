import pandas as pd
from app import main
from flask import jsonify, request
from app.utilities import endDate
from app.dataframes import df_Index_Constituents, df_FTSEJSE_Index_Series, df_Industry_Classification_Benchmark, df_BA_Beta_Output

app = main.app

@app.route('/api/index/')
def getIndexInstruments():
    qry_args = request.args
    index_name = qry_args.get("indexName")
    date = qry_args.get("date")
    endDate = qry_args.get("endDate")

    qry = '{0} New == {0} and Date >= "{1}" and Date <= "{2}"'.format(index_name, date, endDate)
    results_df = df_Index_Constituents.qry(query, inplace = True)
    results_df = results_df[['Instrument', 'Gross Market Capitilisation']]
    results_df.sort_values(by=['Gross Market Capitalisation'], inplace=True)

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp

@app.route('/api/index/index-types')
def getIndexType():
    qry_args = request.args
    index_name = qry_args.get("indexName")
    date = qry_args.get("date")
    results_df = df_FTSEJSE_Index_Series["Index Type"].unique()
    results_df.sort_values(inplace=True)

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp

@app.route('/api/index/super-sector')
def getIndexSuperSector():
    qry_args = request.args
    index_name = qry_args.get("indexName")
    date = qry_args.get("date")
    endDate = qry_args.get("date")

    qry = '{0} New == {0} and Date >= "{1}" and Date <= "{2}"'.format(index_name, date, endDate)
    merged_df = df_Index_Constituents.merge(df_Industry_Classification_Benchmark, left_on='ICB Sub-Sector', right_on='Sub-Sector Code', how='left')
    results_df = merged_df.query(query, inplace = True)
    results_df.sort_values(inplace=True)

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp


@app.route('/api/index/<string:indextype>')
def getIndex(indexType):
    qry_args = request.args
    date = qry_args.get("date")
    endDate = qry_args.get("date")

    qry = 'Date >= "{1}" and Date <= "{2}"'.format(date, endDate)
    df_Inst = df_FTSEJSE_Index_Series.loc[df_FTSEJSE_Index_Series['Index Type'] == {1}].format(indexType)
    df_Inst_Ind = df_Inst[["Index Code", "Index Name"]]

    new_dict = {}
    df_Index = pd.unique(df_BA_Beta_Output['Index'])
    for x in df_Index:
        new_dict[x] = df_BA_Beta_Output[df_BA_Beta_Output['Index'] == x]
        x = new_dict[x]
        x = x.query(query, inplace = True)

    