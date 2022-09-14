import pandas as pd
from app import main
from flask import request
import json
from app.utilities import retEndDate
from app.dataframes import df_Index_Constituents, df_FTSEJSE_Index_Series, df_Industry_Classification_Benchmark, df_BA_Beta_Output

app = main.app

@app.route('/api/index/', methods=['GET'])
def getIndexInstruments():
    qry_args = request.args
    index_name = qry_args.get("indexName")
    date = qry_args.get("date")
    endDate = retEndDate(str(date))

    index_name_search = '{0} New'.format(index_name)

    index_const_srt = df_Index_Constituents.set_index([index_name_search])
    index_const_srt = index_const_srt.loc[index_name]
    index_const_srt.reset_index(inplace=True)
    ind_const_srt = index_const_srt.set_index(['Date']).sort_index(level=["Date"], ascending=[False])
    ind_const_sub_df = ind_const_srt.loc[date:endDate]

    ind_const_sub_df.reset_index(inplace=True)
    ind_const_sub_df.set_index(['Instrument', 'Gross Market Capitalisation'])
    
    results_df = ind_const_sub_df.loc[:, ['Instrument', 'Gross Market Capitalisation']]
    results_df.sort_values(by=['Gross Market Capitalisation'], inplace=True)

    resp = results_df.to_json(orient='records') 
    
    return resp

@app.route('/api/index/index-types', methods=['GET'])
def getIndexType():
    index_types_ls = df_FTSEJSE_Index_Series["Index Type"].unique().tolist()
    
    results_dict = {}
    results_dict = {k:v for (k, v) in enumerate(index_types_ls)}
    
    resp = json.dumps(results_dict)
    
    return resp

@app.route('/api/index/super-sector', methods=['GET'])
def getIndexSuperSector():
    qry_args = request.args
    index_name = qry_args.get("indexName")
    date = qry_args.get("date")
    endDate = retEndDate(str(date))

    index_name_search = '{0} New'.format(index_name)

    index_const_srt = df_Index_Constituents.set_index([index_name_search])
    index_const_srt = index_const_srt.loc[index_name]
    index_const_srt.reset_index(inplace=True)
    ind_const_srt = index_const_srt.set_index(['Date']).sort_index(level=["Date"], ascending=[False])
    ind_const_sub_df = ind_const_srt.loc[date:endDate]

    merged_df = ind_const_sub_df.merge(df_Industry_Classification_Benchmark, left_on='ICB Sub-Sector', right_on='Sub-Sector Code', how='left')
    merged_df_new = merged_df.loc[:, ['Super Sector Code', 'Gross Market Capitalisation']]

    results_df = merged_df_new.groupby(['Super Sector Code']).sum()

    resp = results_df.to_json(orient='records')
    
    resp.status_code = 200
    
    return resp

'''
@app.route('/api/index/<indextype>')
def getIndex(indexType):
    qry_args = request.args
    date = qry_args.get("date")
    endDate = retEndDate(str(date))

    qry = 'Date >= "{1}" and Date <= "{2}"'.format(date, endDate)
    df_Inst = df_FTSEJSE_Index_Series.loc[df_FTSEJSE_Index_Series['Index Type'] == {1}].format(indexType)
    df_Inst_Ind = df_Inst[["Index Code", "Index Name"]]

    new_dict = {}
    df_Index = pd.unique(df_BA_Beta_Output['Index'])

    for x in df_Index:
        new_dict[x] = df_BA_Beta_Output[df_BA_Beta_Output['Index'] == x]
        x = new_dict[x]
        x = x.query(qry, inplace = True) 
'''

    