'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages

#################################################

dataDfList = []
dfColnames = []
meanList = []
EvScoreList = []


dataDfList.append(pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_nrSprotExpGOAv2_against_myDB.xlsx")))
#			dataDfList.append(pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_sprot_clstrd_ref_myAlgo_descs.xlsx")))


colnames = pd.Series(["AHRD Score","SwissProt Score"])

####extract the columns names as they are placed in 3rd row
for i in range(0,1):
	dfColnames = dataDfList[i].ix[2]
	rownames = pd.Series(range(1,len(dataDfList[i])-2))
	dataDfList[i] = dataDfList[i].rename(columns=dfColnames).drop(dataDfList[i].index[:3])
	dataDfList[i].index = rownames
	dataDfList[i] = dataDfList[i]["Evaluation-Score"] #filter columns except evaluation scores
	dataDfList[i].columns = colnames
	dataDfList[i] = dataDfList[i].astype(float)


################mean calculation#######################

for i in range(0,1):
	meanList = []
	for j in range(0,2):
		meanList.append(dataDfList[i][colnames[j]].mean())
	print "mean: " , meanList



#######AHRD scores histogram plot of 4 different experiments##########

#			result = pd.DataFrame({"eggNOG Descriptions Evaluation Score": dataDfList[0].iloc[:,0] , "myAlgo Descriptions Evaluation Score": dataDfList[1].iloc[:,0]})

#			cols = result.columns

#			result.plot(alpha = 0.4, kind='hist', color=['indigo', 'green'])
#			plt.ylabel("Frequency")
#			plt.xlabel("AHRD Score")
#			plt.legend(cols, loc = 'best') 
#			plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_sprotClstrd.jpg")
			#plt.show()
#			plt.close()



####################################################################################################
##########AHRD scores scatter plot matrix of 4 different experiments for all proteins###############

#			data = {'eggNOG': dataDfList[0].iloc[:,0], 'myAlgo': dataDfList[1].iloc[:,0]}
#			allAhrd = pd.DataFrame(data, columns=['eggNOG', 'myAlgo'])
			#data = {'both': bothScoreDf['AHRD Score'], 'token': tokScoreDf['AHRD Score'], 'none': noneScoreDf['AHRD Score']}
			#allAhrd = pd.DataFrame(data, columns=['both', 'token', 'none'])

#			plt.title('Evaluation Scores Comparison')
			#filtDesScore = desScoreDf.iloc[0:100,]
#			allCompare = scatter_matrix(allAhrd, alpha = 0.5, figsize=(15,15), diagonal = None) 
			#plt.legend(desScoreDf.columns) 

			###better reshape
#			[s.xaxis.label.set_rotation(45) for s in allCompare.reshape(-1)] #Change label rotation
#			[s.yaxis.label.set_rotation(45) for s in allCompare.reshape(-1)]

#			[s.get_yaxis().set_label_coords(-0.1,0.5) for s in allCompare.reshape(-1)] #May need to offset label when rotating to prevent overlap of figure

#			[s.set_xticks(()) for s in allCompare.reshape(-1)] #Hide all ticks
#			[s.set_yticks(()) for s in allCompare.reshape(-1)]
			#plt.show()
#			plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_sprotClstrd.jpg")
#			plt.close()

