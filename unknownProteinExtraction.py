'''
@auther: Samaneh Jozashoori
@analysis on AHRD result on sprot_batch3 using both blacklists

'''
import re
import numpy as np
import pandas as pd
from Bio import SeqIO
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import decimal as dc

#seperate proteins in swissprot database with "uncharacterized protein" tag from others
ref = "../data/reference/non_red_sprot_batch_3_references.fasta"
seqs = SeqIO.parse(ref, "fasta")

pattern1 = "Uncharacterized"
pattern2 = "protein"

refMatchedDesList = []
refUnMatchedDesList = []
refMatchedNameList = []
refUnMatchedNameList = []
refMatchedIds = []

flag = False
allIds = dict()

for seq in seqs:
	allIds.update({seq.id : [seq.name,(seq.description).strip(seq.name)]})
	for w in seq.description.split(" "):
		if re.match(pattern1, w):
			flag = True
		elif flag == True and re.match(pattern2, w):
			if seq.id not in refMatchedIds:
				refMatchedDesList.append((seq.description).strip(seq.name))	
				refMatchedNameList.append(seq.name)
				refMatchedIds.append(seq.id)
				count = False
for k in allIds.keys():
	if k not in refMatchedIds:
		refUnMatchedDesList.append(allIds.get(k)[1])
		refUnMatchedNameList.append(allIds.get(k)[0])

refUncharacterizedProteins = pd.DataFrame({"Protein-Accession": refMatchedNameList, "Human-Readable-Description": refMatchedDesList})
refDesProteins = pd.DataFrame({"Protein-Accession": refUnMatchedNameList, "Human-Readable-Description": refUnMatchedDesList})

####################################write the seperation results in xlsx file#################################################
###################################################### BOTH ##################################################################

#seperate proteins in AHRD result with "unknown protein" from those with normal descriptions
allDesDf_both = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))

allDesColnames_both = allDesDf_both.ix[2]
allDesDf_both = allDesDf_both.rename(columns=allDesColnames_both).drop(allDesDf_both.index[:3])

rownames_both = pd.Series(range(1,1493))
allDesDf_both.index = rownames_both

#select multiple columns
allDesDf_both = allDesDf_both[["Protein-Accession","Human-Readable-Description"]]

ahrdUnknownProteins_both = allDesDf_both[allDesDf_both["Human-Readable-Description"]=="Unknown protein"] #select proteins with unknown descriptions
ahrdDesProteins_both = allDesDf_both[allDesDf_both["Human-Readable-Description"]!="Unknown protein"] #select proteins with descriptions

descSeperation_both = ExcelWriter("/home/samaneh/AHRD/outputs/descExtractedFromSprot3_both.xlsx")			
				
ahrdUnknownProteins_both.to_excel(descSeperation_both, "ahrdUnknownProteins")
ahrdDesProteins_both.to_excel(descSeperation_both, "ahrdNormalDescriptions")
refUncharacterizedProteins.to_excel(descSeperation_both, "refUncharacterizedProteins")
refDesProteins.to_excel(descSeperation_both, "refNormalDescriptions")

descSeperation_both.save()


####################################write the seperation results in xlsx file#################################################
################################################# NO BLACKLIST ###############################################################

#seperate proteins in AHRD result with "unknown protein" from those with normal descriptions
allDesDf_noBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_3.xlsx"))

allDesColnames_noBlacklist = allDesDf_noBlacklist.ix[2]
allDesDf_noBlacklist = allDesDf_noBlacklist.rename(columns=allDesColnames_noBlacklist).drop(allDesDf_noBlacklist.index[:3])

rownames_noBlacklist = pd.Series(range(1,1493))
allDesDf_noBlacklist.index = rownames_noBlacklist

#select multiple columns
allDesDf_noBlacklist = allDesDf_noBlacklist[["Protein-Accession","Human-Readable-Description"]]

ahrdUnknownProteins_noBlacklist = allDesDf_noBlacklist[allDesDf_noBlacklist["Human-Readable-Description"]=="Unknown protein"] #select proteins with unknown descriptions
ahrdDesProteins_noBlacklist = allDesDf_noBlacklist[allDesDf_noBlacklist["Human-Readable-Description"]!="Unknown protein"] #select proteins with descriptions

descSeperation_noBlacklist = ExcelWriter("/home/samaneh/AHRD/outputs/descExtractedFromSprot3_noBlacklist.xlsx")			
				
ahrdUnknownProteins_noBlacklist.to_excel(descSeperation_noBlacklist, "ahrdUnknownProteins")
ahrdDesProteins_noBlacklist.to_excel(descSeperation_noBlacklist, "ahrdNormalDescriptions")
refUncharacterizedProteins.to_excel(descSeperation_noBlacklist, "refUncharacterizedProteins")
refDesProteins.to_excel(descSeperation_noBlacklist, "refNormalDescriptions")

descSeperation_noBlacklist.save()

####################################write the seperation results in xlsx file#################################################
################################################ DESCLINE BLACKLIST ##########################################################

#seperate proteins in AHRD result with "unknown protein" from those with normal descriptions
allDesDf_desBlacklist = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_descline_3.xlsx"))

allDesColnames_desBlacklist = allDesDf_desBlacklist.ix[2]
allDesDf_desBlacklist = allDesDf_desBlacklist.rename(columns=allDesColnames_noBlacklist).drop(allDesDf_noBlacklist.index[:3])

rownames_desBlacklist = pd.Series(range(1,1493))
allDesDf_desBlacklist.index = rownames_desBlacklist

#select multiple columns
allDesDf_desBlacklist = allDesDf_desBlacklist[["Protein-Accession","Human-Readable-Description"]]

ahrdUnknownProteins_desBlacklist = allDesDf_desBlacklist[allDesDf_desBlacklist["Human-Readable-Description"]=="Unknown protein"] #select proteins with unknown descriptions
ahrdDesProteins_desBlacklist = allDesDf_desBlacklist[allDesDf_desBlacklist["Human-Readable-Description"]!="Unknown protein"] #select proteins with descriptions

descSeperation_desBlacklist = ExcelWriter("/home/samaneh/AHRD/outputs/descExtractedFromSprot3_desBlacklist.xlsx")			
				
ahrdUnknownProteins_desBlacklist.to_excel(descSeperation_desBlacklist, "ahrdUnknownProteins")
ahrdDesProteins_desBlacklist.to_excel(descSeperation_desBlacklist, "ahrdNormalDescriptions")
refUncharacterizedProteins.to_excel(descSeperation_desBlacklist, "refUncharacterizedProteins")
refDesProteins.to_excel(descSeperation_desBlacklist, "refNormalDescriptions")

descSeperation_desBlacklist.save()


###############################################################################################################################
################################### confusion matrix PLOT ################################
#predicted = [# of unknown proteins, # of normal descriptions]
#actual = [# of uncharacterized proteins, # of normal descriptions]

###predicted = [len(ahrdUnknownProteins), len(ahrdDesProteins)]
###actual = [len(refMatchedNameList), len(refUnMatchedNameList)]
###print predicted, actual

###confMat = confusion_matrix(actual, predicted, labels=["unknown proteins","normal descriptions"])

###def plotConfusionMatrix(confMat, title="Confusion Matrix"):
###	plt.imshow(confMat, interpolation="nearest")
###	plt.title(title)
###	plt.colorbar()

###plotConfusionMatrix(confMat)


###############################################################################################################################
################################################### CONFUSION MATRIX ##########################################################

########################### BOTH ############################

TP_both= FP_both= TN_both= FN_both = 0
falsePositiveList = []
file = []

# True Negative: number of ahrd Normal predictions that are Normal in reference
for pro in ahrdDesProteins_both.iloc[:,0]:
	if pro in refUnMatchedNameList:
		TN_both = TN_both + 1
	else:
		pass	
# False Positive: number of ahrd Uknown predictions that are Normal in reference
for pro in ahrdUnknownProteins_both.iloc[:,0]:
	if pro in refUnMatchedNameList:	
		FP_both = FP_both + 1
	else:
		pass

# False Negative: number of ahrd Normal predictions that are Uncharacterized in reference
for pro in ahrdDesProteins_both.iloc[:,0]:
	if pro in refMatchedNameList:
		FN_both = FN_both + 1
	else:
		pass

# True Positive: number of ahrd Unknown predictions that are Uncharacterized in reference
for pro in ahrdUnknownProteins_both.iloc[:,0]:
	if pro in refMatchedNameList:
		TP_both = TP_both + 1
	else:
		falsePositiveList.append(pro)

falsePositiveFile =  open(("/home/samaneh/AHRD/outputs/falsePositiveDescriptions.txt"),"w")
for n in falsePositiveList:
	file.append(refDesProteins[refDesProteins["Protein-Accession"]==n].iloc[0,0])


falsePositiveFile.write("\n".join(file))


######################### NO BLACKLIST #######################

TP_noBlacklist= FP_noBlacklist= TN_noBlacklist= FN_noBlacklist = 0

falsePositiveList_no = []
file_no = []

# True Negative: number of ahrd Normal predictions that are Normal in reference
for pro in ahrdDesProteins_noBlacklist.iloc[:,0]:
	if pro in refUnMatchedNameList:
		TN_noBlacklist = TN_noBlacklist + 1
	else:
		pass	
# False Positive: number of ahrd Uknown predictions that are Normal in reference
for pro in ahrdUnknownProteins_noBlacklist.iloc[:,1]:
	if pro in refUnMatchedNameList:	
		FP_noBlacklist = FP_noBlacklist + 1
	else:
		pass

# False Negative: number of ahrd Normal predictions that are Uncharacterized in reference
for pro in ahrdDesProteins_noBlacklist.iloc[:,0]:
	if pro in refMatchedNameList:
		FN_noBlacklist = FN_noBlacklist + 1
	else:
		pass

# True Positive: number of ahrd Unknown predictions that are Uncharacterized in reference
for pro in ahrdUnknownProteins_noBlacklist.iloc[:,0]:
	if pro in refMatchedNameList:
		TP_noBlacklist = TP_noBlacklist + 1
	else:
		falsePositiveList_no.append(pro)

falsePositiveFile_no =  open(("/home/samaneh/AHRD/outputs/falsePositiveDescriptions_no.txt"),"w")
for n in falsePositiveList_no:
	file_no.append(refDesProteins[refDesProteins["Protein-Accession"]==n].iloc[0,0])
falsePositiveFile_no.write("\n".join(file_no))

########################## DESCLINE ###########################

TP_desBlacklist= FP_desBlacklist= TN_desBlacklist= FN_desBlacklist = 0

# True Negative: number of ahrd Normal predictions that are Normal in reference
for pro in ahrdDesProteins_desBlacklist.iloc[:,0]:
	if pro in refUnMatchedNameList:
		TN_desBlacklist = TN_desBlacklist + 1
	else:
		pass	
# False Positive: number of ahrd Uknown predictions that are Normal in reference
for pro in ahrdUnknownProteins_desBlacklist.iloc[:,0]:
	if pro in refUnMatchedNameList:	
		FP_desBlacklist = FP_desBlacklist + 1
	else:
		pass

# False Negative: number of ahrd Normal predictions that are Uncharacterized in reference
for pro in ahrdDesProteins_desBlacklist.iloc[:,0]:
	if pro in refMatchedNameList:
		FN_desBlacklist = FN_desBlacklist + 1
	else:
		pass

# True Positive: number of ahrd Unknown predictions that are Uncharacterized in reference
for pro in ahrdUnknownProteins_desBlacklist.iloc[:,0]:
	if pro in refMatchedNameList:
		TP_desBlacklist = TP_desBlacklist + 1
	else:
		pass


#print len(allDesDf.index)
#print "unknown proteins: ", len(ahrdUnknownProteins_desBlacklist), "normal descriptions: ", len(ahrdDesProteins_desBlacklist) 
#print "TP: ", TPcount_desBlacklist, "FP: ", FPcount_desBlacklist, "TN: ",TNcount_desBlacklist, "FN: ", FNcount_desBlacklist

############

#sensitivity = true positive rate
sensitivity = 100*(dc.Decimal(TP_both) / (dc.Decimal(TP_both) + dc.Decimal(FN_both)))

#specificity = true negative rate
specificity = 100*(dc.Decimal(TN_both) / (dc.Decimal(TN_both) + dc.Decimal(FP_both)))

#precision = positive prediction value
precision = 100*(dc.Decimal(TP_both) / (dc.Decimal(TP_both) + dc.Decimal(FP_both)))

#false discovery rate
fdr = 100*(dc.Decimal(FP_both) / (dc.Decimal(FP_both) + dc.Decimal(TP_both)))

#print "sensitivity= ", sensitivity, "specificity", specificity, "precision", precision, "fdr", fdr



