'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages


###Read Data

dataDfList = []
dfColnames = []
meanList = []
EvScoreList = []

### sprot3 old blacklist: index0, sprot3 new blacklist: index1, sprot4 old blacklist: index2, sprot4 new blacklist: index3

dataDfList.append(pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_1.xlsx")))
dataDfList.append(pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_1_newBlacklist.xlsx")))


colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

####extract the columns names as they are placed in 3rd row
for i in range(0,2):
	dfColnames = dataDfList[i].ix[2]
	rownames = pd.Series(range(1,len(dataDfList[i])-2))
	dataDfList[i] = dataDfList[i].rename(columns=dfColnames).drop(dataDfList[i].index[:3])
	dataDfList[i].index = rownames
	dataDfList[i] = dataDfList[i]["Evaluation-Score"] #filter columns except evaluation scores
	dataDfList[i].columns = colnames
	dataDfList[i] = dataDfList[i].astype(float)

################mean calculation#######################

for i in range(0,2):
	meanList = []
	for j in range(0,2):
		meanList.append(dataDfList[i][colnames[j]].mean())
	#print "mean::" , meanList

#meanOut = open("/home/samaneh/AHRD/outputs/meanOutputs_3","w")
#meanOut.write(' '.join(("bothAhrdMean:",str(bothAhrdMean),"bothTairMean:",str(bothTairMean),"bothSprotMean:",str(bothSprotMean),"bothTremMean:",str(bothTremMean),"\t","tokAhrdMean:",str(tokAhrdMean),"tokTairMean:",str(tokTairMean),"tokSprotMean:",str(tokSprotMean),"tokTremMean:",str(tokTremMean),"\t","noneAhrdMean:",str(noneAhrdMean),"noneTairMean:",str(noneTairMean),"noneSprotMean:",str(noneSprotMean),"noneTremMean:",str(noneTremMean))))
#meanOut.close()


#######AHRD scores histogram plot of 4 different experiments##########
result = pd.DataFrame({"sprot3-oldBlacklist Evaluation Score": dataDfList[0].iloc[:,0], "sprot3-newBlacklist Evaluation Score": dataDfList[1].iloc[:,0]})

cols = result.columns

result.plot(alpha = 0.4, kind='hist', color=['yellow','purple'])
plt.ylabel("Frequency")
plt.xlabel("AHRD Score")
plt.legend(cols, loc = 'best') 
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_tair1_blacklists.jpg")
#plt.show()
plt.close()
