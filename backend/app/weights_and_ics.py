'''
    Author: Daiyaan Salie   
     
'''
import numpy as np
import pandas as pd
from app.dataframes import df_Index_Constituents

tbl_Index_Constituents = df_Index_Constituents

def getICsAndWeights(rDate,IndexCode,tbl_Index_Constituents):
    '''
        What function does:
            

        Args:
            table (str): dbo.tbl_Index_Constituents.
            datetime (date): rDate.
            string (str): indexCode.            

        Returns:
    

        # Add a section detailing what errors might be raised
        Raises:
    
    '''
    #rDate will be supplied by the user: consisting of year and Quarter 
    rDate = rDate
    rDate = pd.to_datetime(rDate, format = "%Y-%m-%d")
    rDate_Quarter = rDate.quarter
    rDate_Year = rDate.year

    #search tbl_Index_Constituents Date column and find Quarter and Year for each date in column
    Dates_Col = tbl_Index_Constituents["Date"]
    Dates_Col = pd.arrays.DatetimeArray(Dates_Col)
    Dates_Col_Quarter = Dates_Col.quarter
    Dates_Col_Year = Dates_Col.year

    #Filter tbl_Index_Constituents using supplied quarter and year data from rData
    tbl_Index_Constituents_Date = tbl_Index_Constituents.loc[(Dates_Col_Quarter == rDate_Quarter) & (Dates_Col_Year == rDate_Year),]


    #IndexCode is provided by user: "ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY" or "ALTI"
    IndexCode = IndexCode #provided as input by the user. "ALSI" for testing purposes

    #function to identify The index column that must be searched
    def Index_Col_Identifier(argument):
        match argument:
            case "FLED":
                return "ALSI New"
            case  "LRGG"|"MIDC"|"SMILC":
                return "Index New"
            case default:
                return argument+" New"
    
    IndexCode_Col = Index_Col_Identifier(IndexCode) #Obtain column name to search relevant rows

    #Filter tbl_Index_Constituents_Date using supplied IndexCode in the column identified from Index_Col_Identifier function
    tbl_Index_Constituents_final = tbl_Index_Constituents_Date[tbl_Index_Constituents_Date[IndexCode_Col] == IndexCode]

    #Generate results table with Shares and corresponding share weights
    Alpha = pd.DataFrame(tbl_Index_Constituents_final.loc[:,"Alpha"])
    Gross_Market_Capitalisation = np.array(tbl_Index_Constituents_final.loc[:,"Gross Market Capitalisation"])
    Weigths = pd.DataFrame(Gross_Market_Capitalisation/np.sum(Gross_Market_Capitalisation))
    Results = pd.concat([Alpha.reset_index(drop=True), Weigths.reset_index(drop=True)],axis=1)
    Results.columns = ['Alpha','Weights']

    return Results