'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages




file = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_1.xlsx"))

colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

tairColnames = file.ix[2]
tairRownames=pd.Series(range(1,(len(file)-2)))
file = file.rename(columns=tairColnames).drop(file.index[:3])
file.index = tairRownames
file = file["Evaluation-Score"]
file.columns = colnames
file = file.astype(float)


################mean calculation#######################

tairMeanList = []

tairMeanList.append([file['AHRD Score'].mean(), file['Tair Score'].mean(), file['SwissProt Score'].mean(), file['Trembl Score'].mean()])

print tairMeanList
