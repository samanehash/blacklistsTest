'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages


####################################### Sprot3 reference ###########################################################
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


################ mean calculation #######################

sprotMeanList = []

for i in range(0,4):
	sprotMeanList.append([sprotList[i]['AHRD Score'].mean(), sprotList[i]['Tair Score'].mean(), sprotList[i]['SwissProt Score'].mean(), sprotList[i]['Trembl Score'].mean()])

print sprotMeanList

#######AHRD scores histogram plot of 4 different experiments##########

sprotAhrdList = []

for i in range(0,4):
	sprotAhrdList.append(sprotList[i].iloc[:,0])


AHRDComparison_filteredSprot3 = pd.DataFrame({ "filtered sprot3 both blacklists AHRD": sprotAhrdList[0],"filtered sprot3 no blacklist AHRD":sprotAhrdList[2] })
AHRDComparison_incBlacklistSprot3 = pd.DataFrame({ "including blacklist's tokens sprot3 both blacklists AHRD": sprotAhrdList[1], "including blacklist's tokens sprot3 no blacklist AHRD":sprotAhrdList[3] })


def histo(dfDict):
	df = dfDict.values()[0]
	cols = df.columns
	df.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
	plt.ylabel("Frequency")
	plt.xlabel("AHRD Score")
	plt.legend(cols, loc = 'best') 
	s = "/home/samaneh/AHRD/outputs/" + dfDict.keys()[0] + ".jpg"
	plt.savefig(s)
	plt.close()


histo(dict({"AHRDComparison_filteredSprot3":AHRDComparison_filteredSprot3}))
histo(dict({"AHRDComparison_incBlacklistSprot3":AHRDComparison_incBlacklistSprot3}))


####################################################################################################
##########AHRD scores scatter plot matrix of 2 different experiments for all proteins###############

####data = {'both_sprot3_incBlacklist': bothSprot3incBlacklist['AHRD Score'], 'no_sprot3_incBlacklist': noSprot3incBlacklist['AHRD Score']}
###allAhrd = pd.DataFrame(data, columns=['both_sprot3_incBlacklist', 'no_sprot3_incBlacklist'])
#print allAhrd

###plt.title('Evaluation Scores Comparison')
#filtDesScore = desScoreDf.iloc[0:100,]
###allCompare = scatter_matrix(allAhrd, alpha = 0.5, figsize=(15,15), diagonal = None) 
#plt.legend(desScoreDf.columns) 

###better reshape
###[s.xaxis.label.set_rotation(45) for s in allCompare.reshape(-1)] #Change label rotation
###[s.yaxis.label.set_rotation(0) for s in allCompare.reshape(-1)]

###[s.get_yaxis().set_label_coords(-0.3,0.5) for s in allCompare.reshape(-1)] #May need to offset label when rotating to prevent overlap of figure

###[s.set_xticks(()) for s in allCompare.reshape(-1)] #Hide all ticks
###[s.set_yticks(()) for s in allCompare.reshape(-1)]
#plt.show()
###plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_Sprot3incBlacklists.jpg")
###plt.close()

####################################### TAIR10 reference ###########################################################
############################################################################################################################
############################################################################################################################

tairList = []
tairColnames = []
tairRownames = []

files = [	pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair1_filtered.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair1_incBlacklist.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_tair1_filtered.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_tair1_incBlacklist.xlsx"))]

colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

for i in range(0,4):
	tairList.append(files[i])
	tairColnames.append(tairList[i].ix[2])
	tairRownames.append(pd.Series(range(1,(len(tairList[i])-2))))
	tairList[i] = tairList[i].rename(columns=tairColnames[i]).drop(tairList[i].index[:3])
	tairList[i].index = tairRownames[i]
	tairList[i] = tairList[i]["Evaluation-Score"]
	tairList[i].columns = colnames
	tairList[i] = tairList[i].astype(float)


################mean calculation#######################

tairMeanList = []

for i in range(0,4):
	tairMeanList.append([tairList[i]['AHRD Score'].mean(), tairList[i]['Tair Score'].mean(), tairList[i]['SwissProt Score'].mean(), tairList[i]['Trembl Score'].mean()])

print tairMeanList

#######AHRD scores histogram plot of 4 different experiments##########

tairAhrdList = []

for i in range(0,4):
	tairAhrdList.append(tairList[i].iloc[:,0])


AHRDComparison_filteredTair1 = pd.DataFrame({ "filtered tair1 both blacklists AHRD": tairAhrdList[0],"filtered tair1 no blacklist AHRD":tairAhrdList[2] })
AHRDComparison_incBlacklistTair1 = pd.DataFrame({ "including blacklist's tokens tair1 both blacklists AHRD": tairAhrdList[1], "including blacklist's tokens tair1 no blacklist AHRD":tairAhrdList[3] })


def histo(dfDict):
	df = dfDict.values()[0]
	cols = df.columns
	df.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
	plt.ylabel("Frequency")
	plt.xlabel("AHRD Score")
	plt.legend(cols, loc = 'best') 
	s = "/home/samaneh/AHRD/outputs/" + dfDict.keys()[0] + ".jpg"
	plt.savefig(s)
	plt.close()


histo(dict({"AHRDComparison_filteredTair1":AHRDComparison_filteredTair1}))
histo(dict({"AHRDComparison_incBlacklistTair1":AHRDComparison_incBlacklistTair1}))

