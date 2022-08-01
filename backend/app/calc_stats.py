from main import create_dataframes
import numpy as np
import pandas as pd
from weights_and_ics import getICsAndWeights
from betas_mkt_spec_vols import getBetasMktAndSpecVols

frames_dict = create_dataframes()

output1 = getICsAndWeights(rDate,IndexCode,dbo_tbl_Index_Constituents)
ICs = output1["Alpha"]
dbo_tbl_BA_Beta_Output = "tbl_BA_Beta_Output"
mktIndexCode = "J203"
output2 = getBetasMktAndSpecVols(rDate,ICs,dbo_tbl_BA_Beta_Output,mktIndexCode)

def CalcStats(weights,betas,specVols,mktVol):

    weights = np.transpose(np.matrix(output1["Weights"]))
    betas = np.transpose(np.matrix(output2["Betas"]))
    specVols = np.transpose(np.matrix(output2["specVols"]))
    mktVol = np.array(output2["mktVol"])
    mktVol = np.average(mktVol) #Assuming the mktVol is the average. NEED TO CONFIRM

    pfBeta = np.matmul(np.transpose(weights),betas)

    sysCov = np.matmul(betas,np.transpose(betas))*(mktVol**2)

    pfSysVol = np.transpose(weights)@betas@np.transpose(betas)@(weights)*(mktVol**2)

    specCov = np.diagflat(specVols)@np.diagflat(specVols)

    pfSpecVol = np.transpose(weights)@(specCov)@weights

    totCov = sysCov + specCov

    pfVol = pfSysVol + pfSpecVol

    Tot = 0

    CorrMat = np.matmul((np.matmul(np.linalg.inv(np.diag(Tot)),(sysCov + specCov))),np.linalg.inv(np.diag(Tot)))