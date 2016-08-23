'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages

########################### TAIR10 BATCH2 ###########################################

tairList = []
tairColnames = []
tairRownames = []

files = [	pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_2.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_token_tair10_2.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_tair10_2.xlsx"))]

colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

for i in range(0,3):
	tairList.append(files[i])
	tairColnames.append(tairList[i].ix[2])
	tairRownames.append(pd.Series(range(1,(len(tairList[i])-2))))
	tairList[i] = tairList[i].rename(columns=tairColnames[i]).drop(tairList[i].index[:3])
	tairList[i].index = tairRownames[i]
	tairList[i] = tairList[i]["Evaluation-Score"]
	tairList[i].columns = colnames
	tairList[i] = tairList[i].astype(float)


###################### mean calculation ###########################

tairMeanList = []

for i in range(0,3):
	tairMeanList.append([tairList[i]['AHRD Score'].mean(), tairList[i]['Tair Score'].mean(), tairList[i]['SwissProt Score'].mean(), tairList[i]['Trembl Score'].mean()])

print "tair2 means:", tairMeanList

#######AHRD scores histogram plot of 3 different experiments##########

tairAhrdList = []

for i in range(0,3):
	tairAhrdList.append(tairList[i].iloc[:,0])


AHRDComparison_tair2 = pd.DataFrame({ "tair2 both blacklists AHRD": tairAhrdList[0],"tair2 token AHRD":tairAhrdList[1], "tair2 no blacklist AHRD":tairAhrdList[2] })


def histo(dfDict):
	df = dfDict.values()[0]
	cols = df.columns
	df.plot(alpha = 0.4, kind='hist', color=['purple','yellow','green'])
	plt.ylabel("Frequency")
	plt.xlabel("AHRD Score")
	plt.legend(cols, loc = 'best') 
	s = "/home/samaneh/AHRD/outputs/" + dfDict.keys()[0] + ".jpg"
	plt.savefig(s)
	plt.close()


histo(dict({"AHRDComparison_tair2":AHRDComparison_tair2}))

####################### scatter plot #################################

data = {'both': tairList[0]['AHRD Score'], 'token': tairList[1]['AHRD Score'], 'none': tairList[2]['AHRD Score']}

allAhrd = pd.DataFrame(data, columns=['both', 'token', 'none'])

plt.title('Evaluation Scores Comparison')

allCompare = scatter_matrix(allAhrd, alpha = 0.5, figsize=(15,15), diagonal = None)  

###better reshape
[s.xaxis.label.set_rotation(45) for s in allCompare.reshape(-1)] #Change label rotation
[s.yaxis.label.set_rotation(0) for s in allCompare.reshape(-1)]

[s.get_yaxis().set_label_coords(-0.3,0.5) for s in allCompare.reshape(-1)] #May need to offset label when rotating to prevent overlap of figure

[s.set_xticks(()) for s in allCompare.reshape(-1)] #Hide all ticks
[s.set_yticks(()) for s in allCompare.reshape(-1)]

plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_Tair_2.jpg")
plt.close()