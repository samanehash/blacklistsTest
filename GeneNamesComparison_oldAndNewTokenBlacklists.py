'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
##############################################################################
########################## sprot3 old token ##################################

ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))
dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"]


gnFile = pd.ExcelFile("/home/samaneh/AHRD/outputs/AllSprotGeneNames.xlsx")
GNs = gnFile.parse(header=None)
GNs = GNs.rename(columns={"GRF5":"Gene Name"})

geneNames = GNs.values.tolist()
###########################################
row1 = 0
writer1 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/GeneNamesAppearedInDescriptions.xlsx")
worksheet1 = writer1.add_worksheet()

geneListOld = []

for record in ahrdResult:
	words = record.split(" ")
	for w in words:	
	### check gene names
		for name in geneNames:
			name = str(name[0])
			if w == name: 
				worksheet1.write(row1,0,w)
				worksheet1.write(row1,1,record)
				row1 = row1 + 1
				if name not in geneListOld:
					geneListOld.append(name)

####################################################################################
############################## sprot3 new token ####################################

ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_sprot3_newTokenBlacklist.xlsx"))
dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"]


gnFile = pd.ExcelFile("/home/samaneh/AHRD/outputs/AllSprotGeneNames.xlsx")
GNs = gnFile.parse(header=None)
GNs = GNs.rename(columns={"GRF5":"Gene Name"})

geneNames = GNs.values.tolist()
###########################################
row1 = 0
writer1 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/GeneNamesAppearedInDescriptionsNewTokenBacklist.xlsx")
worksheet1 = writer1.add_worksheet()

geneListNew = []

for record in ahrdResult:
	words = record.split(" ")
	for w in words:	
	### check gene names
		for name in geneNames:
			name = str(name[0])
			if w == name: 
				worksheet1.write(row1,0,w)
				worksheet1.write(row1,1,record)
				row1 = row1 + 1
				if name not in geneListNew:
					geneListNew.append(name)

######################################## compare #####################################
for g in geneListOld:
	 if g not in geneListNew:
	 	print g
print "new: "

for gp in geneListNew:
	if gp not in geneListOld:
		print gp	 	

