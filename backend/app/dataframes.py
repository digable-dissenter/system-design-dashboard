<<<<<<< HEAD
from app import main
import pandas as pd

tbl_Industry_Classification_Benchmark = main.frames_dict["dbo_tbl_Industry_Classification_Benchmark"]
tbl_FTSEJSE_Index_Series = main.frames_dict["dbo_tbl_FTSEJSE_Index_Series"]
tbl_EOD_Equity_Data = main.frames_dict["dbo_tbl_EOD_Equity_Data"]
tbl_EOD_Interest_Rate_Data = main.frames_dict["dbo_tbl_EOD_Interest_Rate_Data"]
tbl_Beta_Output = main.frames_dict["dbo_tbl_Beta_Output"]
tbl_BA_Beta_Output = main.frames_dict["dbo_tbl_BA_Beta_Output"]
tbl_Index_Constituents = main.frames_dict["dbo_tbl_Index_Constituents"]
=======
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
>>>>>>> 40c1656f989b06907c813790f61474f85ce1b478
