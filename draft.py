'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages


#######################################Sprot3 filtered reference ###########################################################
############################################################################################################################
############################################################################################################################

sprotList = []
sprotColnames = []
sprotRownames = []

files = [	pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_sprot3_filtered.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_sprot3_incBlacklist.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_sprot3_filtered.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_sprot3_incBlacklist.xlsx"))]

colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

for i in range(0,4):
	sprotList.append(files[i])
	sprotColnames.append(sprotList[i].ix[2])
	sprotRownames.append(pd.Series(range(1,(len(sprotList[i])-2))))
	sprotList[i] = sprotList[i].rename(columns=sprotColnames[i]).drop(sprotList[i].index[:3])
	sprotList[i].index = sprotRownames[i]
	sprotList[i] = sprotList[i]["Evaluation-Score"]
	sprotList[i].columns = colnames
	sprotList[i] = sprotList[i].astype(float)


################mean calculation#######################

sprotMeanList = []

for i in range(0,4):
	sprotMeanList.append([sprotList[i]['AHRD Score'].mean(), sprotList[i]['Tair Score'].mean(), sprotList[i]['SwissProt Score'].mean(), sprotList[i]['Trembl Score'].mean()])

#print sprotMeanList

#######AHRD scores histogram plot of 4 different experiments##########

sprotAhrdList = []

for i in range(0,4):
	sprotAhrdList.append(sprotList[i].iloc[:,0])


AHRDComparison_filteredSprot3 = pd.DataFrame({ "filtered sprot3 both blacklists AHRD": sprotAhrdList[0],"filtered sprot3 sprot3 no blacklist AHRD":sprotAhrdList[2] })
AHRDComparison_incBlacklistSprot3 = pd.DataFrame({ "including blacklist's tokens sprot3 both blacklists AHRD": sprotAhrdList[1], "including blacklist's tokens sprot3 no blacklist AHRD":sprotAhrdList[3] })


def histo(df):
	cols = df.columns
	df.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
	plt.ylabel("Frequency")
	plt.xlabel("AHRD Score")
	plt.legend(cols, loc = 'best') 
	s = "/home/samaneh/AHRD/outputs" + df ???? + ".jpg"
	plt.savefig(s)
	plt.close()


histo(AHRDComparison_filteredSprot3)
histo(AHRDComparison_incBlacklistSprot3)



