'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages


#######################################Sprot3 including balcklist reference ################################################
############################################################################################################################
############################################################################################################################

###Read Data
bothSprot3incBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_batch_3_incBlacklist.xlsx")) # AHRD tsv outputs are converted to xlsx and are read here
noSprot3incBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_batch_3_incBlacklist.xlsx"))
###test
#ind = bothScore.index #return row names
#col = bothScore.columns #return column names
##
bothSprot3incBlacklistColnames = bothSprot3incBlacklist.ix[2] #extract the columns names as they are placed in 3rd row
noSprot3incBlacklistColnames = noSprot3incBlacklist.ix[2]


rownames_bothSprot3incBlacklist = pd.Series(range(1,(len(bothSprot3incBlacklist)-2)))
rownames_noSprot3incBlacklist = pd.Series(range(1,(len(noSprot3incBlacklist)-2)))


bothSprot3incBlacklist = bothSprot3incBlacklist.rename(columns=bothSprot3incBlacklistColnames).drop(bothSprot3incBlacklist.index[:3]) #remove first two blancked rows and rename columns to real columns names
bothSprot3incBlacklist.index = rownames_bothSprot3incBlacklist #rename rows to start from 1
noSprot3incBlacklist = noSprot3incBlacklist.rename(columns=noSprot3incBlacklistColnames).drop(noSprot3incBlacklist.index[:3])
noSprot3incBlacklist.index = rownames_noSprot3incBlacklist


bothSprot3incBlacklist = bothSprot3incBlacklist["Evaluation-Score"] #filter columns except evaluation scores:
noSprot3incBlacklist = noSprot3incBlacklist["Evaluation-Score"]



colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])


bothSprot3incBlacklist.columns = colnames
bothSprot3incBlacklist = bothSprot3incBlacklist.astype(float)
noSprot3incBlacklist.columns = colnames
noSprot3incBlacklist = noSprot3incBlacklist.astype(float)


#######################################################
################mean calculation#######################
###both Sprot3 incBlacklist
bothSprot3incBlacklist_AhrdMean = bothSprot3incBlacklist['AHRD Score'].mean()
bothSprot3incBlacklist_TairMean = bothSprot3incBlacklist['Tair Score'].mean()
bothSprot3incBlacklist_SprotMean = bothSprot3incBlacklist['SwissProt Score'].mean()
bothSprot3incBlacklist_TremMean = bothSprot3incBlacklist['Trembl Score'].mean()

###no Sprot3 incBlacklist
noSprot3incBlacklist_AhrdMean = noSprot3incBlacklist['AHRD Score'].mean()
noSprot3incBlacklist_TairMean = noSprot3incBlacklist['Tair Score'].mean()
noSprot3incBlacklist_SprotMean = noSprot3incBlacklist['SwissProt Score'].mean()
noSprot3incBlacklist_TremMean = noSprot3incBlacklist['Trembl Score'].mean()


#meanOut = open("/home/samaneh/AHRD/outputs/meanOutputs_filteredReference3","w")
#meanOut.write(' '.join(("bothAhrdMean:",str(bothAhrdMean),"bothTairMean:",str(bothTairMean),"bothSprotMean:",str(bothSprotMean),"bothTremMean:",str(bothTremMean),"\t","tokAhrdMean:",str(tokAhrdMean),"tokTairMean:",str(tokTairMean),"tokSprotMean:",str(tokSprotMean),"tokTremMean:",str(tokTremMean),"\t","noneAhrdMean:",str(noneAhrdMean),"noneTairMean:",str(noneTairMean),"noneSprotMean:",str(noneSprotMean),"noneTremMean:",str(noneTremMean))))
#meanOut.close()
#print "bothAhrdMean:",bothAhrdMean,"bothTairMean:",bothTairMean,"bothSprotMean:",bothSprotMean,"bothTremMean:",bothTremMean,"\t","tokAhrdMean:",tokAhrdMean,"tokTairMean:",tokTairMean,"tokSprotMean:",tokSprotMean,"tokTremMean:",tokTremMean,"\t","noneAhrdMean:",noneAhrdMean,"noneTairMean:",noneTairMean,"noneSprotMean:",noneSprotMean,"noneTremMean:",noneTremMean


######################################################################
#######AHRD scores histogram plot of 4 different experiments##########

ahrd_bothSprot3incBlacklist = bothSprot3incBlacklist.iloc[:,0]
ahrd_noSprot3incBlacklist = noSprot3incBlacklist.iloc[:,0]
 


result = pd.DataFrame({"Sprot3 incBlacklist_both blacklists AHRD": ahrd_bothSprot3incBlacklist, "Sprot3 incBlacklist_no blacklist AHRD": ahrd_noSprot3incBlacklist})

#cols = transResult.index
cols = result.columns

result.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
plt.ylabel("Frequency")
plt.xlabel("AHRD Score")
plt.legend(cols, loc = 'best') 
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_Sprot3incBlacklist.jpg")
#plt.show()
plt.close()

####################################################################################################
##########AHRD scores scatter plot matrix of 2 different experiments for all proteins###############

data = {'both_sprot3_incBlacklist': bothSprot3incBlacklist['AHRD Score'], 'no_sprot3_incBlacklist': noSprot3incBlacklist['AHRD Score']}
allAhrd = pd.DataFrame(data, columns=['both_sprot3_incBlacklist', 'no_sprot3_incBlacklist'])
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
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_Sprot3incBlacklists.jpg")
plt.close()



#######################################Tair1 filtered reference ############################################################
############################################################################################################################
############################################################################################################################

###Read data
bothTair1Filtered = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair_1_incBlacklist.xlsx"))
noTair1Filtered = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_tair_1_incBlacklist.xlsx"))


bothTair1FilteredColnames = bothTair1Filtered.ix[2]
noTair1FilteredColnames = noTair1Filtered.ix[2]

rownames_bothTair1Filtered = pd.Series(range(1,(len(bothTair1Filtered)-2)))
rownames_noTair1Filtered = pd.Series(range(1,(len(noTair1Filtered)-2)))

bothTair1Filtered = bothTair1Filtered.rename(columns=bothTair1FilteredColnames).drop(bothTair1Filtered.index[:3])
bothTair1Filtered.index = rownames_bothTair1Filtered
noTair1Filtered = noTair1Filtered.rename(columns=noTair1FilteredColnames).drop(noTair1Filtered.index[:3])
noTair1Filtered.index = rownames_noTair1Filtered


bothTair1Filtered = bothTair1Filtered["Evaluation-Score"]
noTair1Filtered = noTair1Filtered["Evaluation-Score"]


colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

bothTair1Filtered.columns = colnames
bothTair1Filtered = bothTair1Filtered.astype(float)
noTair1Filtered.columns = colnames
noTair1Filtered = noTair1Filtered.astype(float)


#######################################################
################mean calculation#######################

###both Tair1 incBlacklist
bothTair1Filtered_AhrdMean = bothTair1Filtered['AHRD Score'].mean()
bothTair1Filtered_TairMean = bothTair1Filtered['Tair Score'].mean()
bothTair1Filtered_SprotMean = bothTair1Filtered['SwissProt Score'].mean()
bothTair1Filtered_TremMean = bothTair1Filtered['Trembl Score'].mean()

###no Tair1 incBlacklist
noTair1Filtered_AhrdMean = noTair1Filtered['AHRD Score'].mean()
noTair1Filtered_TairMean = noTair1Filtered['Tair Score'].mean()
noTair1Filtered_SprotMean = noTair1Filtered['SwissProt Score'].mean()
noTair1Filtered_TremMean = noTair1Filtered['Trembl Score'].mean()

######################################################################
#######AHRD scores histogram plot of 4 different experiments##########

ahrd_bothTair1Filtered = bothTair1Filtered.iloc[:,0]
ahrd_noTair1Filtered = noTair1Filtered.iloc[:,0]
 


result = pd.DataFrame({"Tair1 Filtered_both blacklists AHRD": ahrd_bothTair1Filtered, "Tair1 Filtered_no blacklist AHRD": ahrd_noTair1Filtered})

#cols = transResult.index
cols = result.columns

result.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
plt.ylabel("Frequency")
plt.xlabel("AHRD Score")
plt.legend(cols, loc = 'best') 
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_Tair1Filtered.jpg")
#plt.show()
plt.close()



######################################################################
#######AHRD scores histogram plot of 2 different experiments##########

data = {'both_tair1_Filtered': bothTair1Filtered['AHRD Score'], 'no_tair1_Filtered': noTair1Filtered['AHRD Score']}

allAhrd = pd.DataFrame(data, columns=['both_tair1_Filtered', 'no_tair1_Filtered'])

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
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_Tair1Filtered.jpg")
plt.close()


#######################################Tair1 including balcklist reference #################################################
############################################################################################################################
############################################################################################################################

###Read data
bothTair1incBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair_1_incBlacklist.xlsx"))
noTair1incBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_tair_1_incBlacklist.xlsx"))


bothTair1incBlacklistColnames = bothTair1incBlacklist.ix[2]
noTair1incBlacklistColnames = noTair1incBlacklist.ix[2]

rownames_bothTair1incBlacklist = pd.Series(range(1,(len(bothTair1incBlacklist)-2)))
rownames_noTair1incBlacklist = pd.Series(range(1,(len(noTair1incBlacklist)-2)))

bothTair1incBlacklist = bothTair1incBlacklist.rename(columns=bothTair1incBlacklistColnames).drop(bothTair1incBlacklist.index[:3])
bothTair1incBlacklist.index = rownames_bothTair1incBlacklist
noTair1incBlacklist = noTair1incBlacklist.rename(columns=noTair1incBlacklistColnames).drop(noTair1incBlacklist.index[:3])
noTair1incBlacklist.index = rownames_noTair1incBlacklist


bothTair1incBlacklist = bothTair1incBlacklist["Evaluation-Score"]
noTair1incBlacklist = noTair1incBlacklist["Evaluation-Score"]


colnames = pd.Series(["AHRD Score","Tair Score","SwissProt Score","Trembl Score"])

bothTair1incBlacklist.columns = colnames
bothTair1incBlacklist = bothTair1incBlacklist.astype(float)
noTair1incBlacklist.columns = colnames
noTair1incBlacklist = noTair1incBlacklist.astype(float)


#######################################################
################mean calculation#######################

###both Tair1 incBlacklist
bothTair1incBlacklist_AhrdMean = bothTair1incBlacklist['AHRD Score'].mean()
bothTair1incBlacklist_TairMean = bothTair1incBlacklist['Tair Score'].mean()
bothTair1incBlacklist_SprotMean = bothTair1incBlacklist['SwissProt Score'].mean()
bothTair1incBlacklist_TremMean = bothTair1incBlacklist['Trembl Score'].mean()

###no Tair1 incBlacklist
noTair1incBlacklist_AhrdMean = noTair1incBlacklist['AHRD Score'].mean()
noTair1incBlacklist_TairMean = noTair1incBlacklist['Tair Score'].mean()
noTair1incBlacklist_SprotMean = noTair1incBlacklist['SwissProt Score'].mean()
noTair1incBlacklist_TremMean = noTair1incBlacklist['Trembl Score'].mean()

######################################################################
#######AHRD scores histogram plot of 4 different experiments##########

ahrd_bothTair1incBlacklist = bothTair1incBlacklist.iloc[:,0]
ahrd_noTair1incBlacklist = noTair1incBlacklist.iloc[:,0]
 


result = pd.DataFrame({"Tair1 incBlacklist_both blacklists AHRD": ahrd_bothTair1incBlacklist, "Tair1 incBlacklist_no blacklist AHRD": ahrd_noTair1incBlacklist})

#cols = transResult.index
cols = result.columns

result.plot(alpha = 0.4, kind='hist', color=['purple','yellow'])
plt.ylabel("Frequency")
plt.xlabel("AHRD Score")
plt.legend(cols, loc = 'best') 
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparison_Tair1incBlacklist.jpg")
#plt.show()
plt.close()



######################################################################
#######AHRD scores histogram plot of 2 different experiments##########

data = {'both_tair1_incBlacklist': bothTair1incBlacklist['AHRD Score'], 'no_tair1_incBlacklist': noTair1incBlacklist['AHRD Score']}

allAhrd = pd.DataFrame(data, columns=['both_tair1_incBlacklist', 'no_tair1_incBlacklist'])

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
plt.savefig("/home/samaneh/AHRD/outputs/AHRDComparisonScatterMatrix_Tair1incBlacklist.jpg")
plt.close()


