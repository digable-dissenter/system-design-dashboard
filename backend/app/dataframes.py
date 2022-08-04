'''
    Author: Kenneth Ssekimpi
'''
from app.main import frames_dict
import pandas as pd

# Retrieving all the necessary dataframes from the dictionary to work with downstream
df_BA_Beta_Output = pd.DataFrame(frames_dict['tbl_BA_Beta_Output'])
df_Beta_Output = pd.DataFrame(frames_dict['tbl_Beta_Output'])
df_EOD_Equity_Data = pd.DataFrame(frames_dict['tbl_EOD_Equity_Data'])
df_EOD_Interest_Rate_Data = pd.DataFrame(frames_dict['tbl_EOD_Interest_Rate_Data'])
df_FTSEJSE_Index_Series = pd.DataFrame(frames_dict['tbl_FTSEJSE_Index_Series'])
df_Index_Constituents = pd.DataFrame(frames_dict['tbl_Index_Constituents'])
df_Industry_Classification_Benchmark = pd.DataFrame(frames_dict['tbl_Industry_Classification_Benchmark'])

# Set indexes and sort
df_BA_Beta_Output = df_BA_Beta_Output.set_index(["Instrument", "Index"])
df_Beta_Output = df_Beta_Output.set_index(["Instrument", "Index"])
df_EOD_Equity_Data = df_EOD_Equity_Data.set_index("Instrument")
df_FTSEJSE_Index_Series = df_FTSEJSE_Index_Series.set_index("Index Code")
df_Index_Constituents = df_Index_Constituents.set_index("Alpha")
df_Industry_Classification_Benchmark = df_Industry_Classification_Benchmark.set_index("Sub-Sector")

from app import indices, sectors, shares
