'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
##########################################################################

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


