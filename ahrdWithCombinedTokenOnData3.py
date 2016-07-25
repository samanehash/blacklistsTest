'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages


###Read Data
bothScoreDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx")) # AHRD tsv outputs are converted to xlsx and are read here
tokScoreDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_combined_token_3.xlsx"))
noneScoreDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_3.xlsx"))
###test
#ind = bothScore.index #return row names
#col = bothScore.columns #return column names
##
bothScoreColnames = bothScoreDf.ix[2] #extract the columns names as they are placed in 3rd row
tokScoreColnames = tokScoreDf.ix[2]
noneScoreColnames = noneScoreDf.ix[2]

rownames = pd.Series(range(1,(len(bothScoreDf)-2)))

bothScoreDf = bothScoreDf.rename(columns=bothScoreColnames).drop(bothScoreDf.index[:3]) #remove first two blancked rows and rename columns to real columns names
bothScoreDf.index = rownames #rename rows to start from 1
tokScoreDf = tokScoreDf.rename(columns=tokScoreColnames).drop(tokScoreDf.index[:3])
tokScoreDf.index = rownames
noneScoreDf = noneScoreDf.rename(columns=noneScoreColnames).drop(noneScoreDf.index[:3])
noneScoreDf.index = rownames

bothScoreDf = bothScoreDf["Evaluation-Score"] #filter columns except evaluation scores:
tokScoreDf = tokScoreDf["Evaluation-Score"]
noneScoreDf = noneScoreDf["Evaluation-Score"]

colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])


bothScoreDf.columns = colnames
bothScoreDf = bothScoreDf.astype(float)
tokScoreDf.columns = colnames
tokScoreDf = tokScoreDf.astype(float)
noneScoreDf.columns = colnames
noneScoreDf = noneScoreDf.astype(float)


#######################################################
################mean calculation#######################
###both score
bothAhrdMean = bothScoreDf['AHRD Score'].mean()
bothTairMean = bothScoreDf['Tair Score'].mean()
bothSprotMean = bothScoreDf['SwissProt Score'].mean()
bothTremMean = bothScoreDf['Trembl Score'].mean()

###token score
tokAhrdMean = tokScoreDf['AHRD Score'].mean()
tokTairMean = tokScoreDf['Tair Score'].mean()
tokSprotMean = tokScoreDf['SwissProt Score'].mean()
tokTremMean = tokScoreDf['Trembl Score'].mean()

###noBlacklist score
noneAhrdMean = noneScoreDf['AHRD Score'].mean()
noneTairMean = noneScoreDf['Tair Score'].mean()
noneSprotMean = noneScoreDf['SwissProt Score'].mean()
noneTremMean = noneScoreDf['Trembl Score'].mean()

meanOut = open("/home/samaneh/AHRD/outputs/meanOutputs_combinedToken_3","w")
meanOut.write(' '.join(("bothAhrdMean:",str(bothAhrdMean),"bothTairMean:",str(bothTairMean),"bothSprotMean:",str(bothSprotMean),"bothTremMean:",str(bothTremMean),"\t","tokAhrdMean:",str(tokAhrdMean),"tokTairMean:",str(tokTairMean),"tokSprotMean:",str(tokSprotMean),"tokTremMean:",str(tokTremMean),"\t","noneAhrdMean:",str(noneAhrdMean),"noneTairMean:",str(noneTairMean),"noneSprotMean:",str(noneSprotMean),"noneTremMean:",str(noneTremMean))))
meanOut.close()
#print "bothAhrdMean:",bothAhrdMean,"bothTairMean:",bothTairMean,"bothSprotMean:",bothSprotMean,"bothTremMean:",bothTremMean,"\t","tokAhrdMean:",tokAhrdMean,"tokTairMean:",tokTairMean,"tokSprotMean:",tokSprotMean,"tokTremMean:",tokTremMean,"\t","noneAhrdMean:",noneAhrdMean,"noneTairMean:",noneTairMean,"noneSprotMean:",noneSprotMean,"noneTremMean:",noneTremMean


######################################################################
#######AHRD scores histogram plot of 4 different experiments##########


ahrdBoth = bothScoreDf.iloc[:,0]
ahrdTok = tokScoreDf.iloc[:,0]
ahrdNone = noneScoreDf.iloc[:,0]
 
result = pd.DataFrame({"Both Evaluation Score": ahrdBoth, "Token Evaluation Score": ahrdTok, "No Blacklist Evaluation Score": ahrdNone})

#cols = transResult.index
cols = result.columns

result.plot(alpha = 0.4, kind='hist', color=['purple','green','yellow'])
plt.ylabel("Frequency")
plt.xlabel("AHRD Score")
plt.legend(cols, loc = 'best') 
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_combinedToken_3.jpg")
#plt.show()
plt.close()

####################################################################################################
##########AHRD scores scatter plot matrix of 4 different experiments for all proteins###############

data = {'both': bothScoreDf['AHRD Score'], 'token': tokScoreDf['AHRD Score'], 'none': noneScoreDf['AHRD Score']}
allAhrd = pd.DataFrame(data, columns=['both', 'token', 'none'])
#print allAhrd

plt.title('Evaluation Scores Comparison')
#filtDesScore = desScoreDf.iloc[0:100,]
allCompare = scatter_matrix(allAhrd, alpha = 0.5, figsize=(15,15), diagonal = None) 
#plt.legend(desScoreDf.columns) 

###better reshape
[s.xaxis.label.set_rotation(45) for s in allCompare.reshape(-1)] #Change label rotation
[s.yaxis.label.set_rotation(0) for s in allCompare.reshape(-1)]

[s.get_yaxis().set_label_coords(-0.3,0.5) for s in allCompare.reshape(-1)] #May need to offset label when rotating to prevent overlap of figure

[s.set_xticks(()) for s in allCompare.reshape(-1)] #Hide all ticks
[s.set_yticks(()) for s in allCompare.reshape(-1)]
#plt.show()
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_combinedToken_3.jpg")
plt.close()