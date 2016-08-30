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

###extract list of geneNames from text file derived from uniprot
geneNames = []
file = open("/home/samaneh/Desktop/uniprot-all.tab","r")
for line in file.readlines():
	if len(line.split())==3:
		gn = line.split()[2]
		if gn not in geneNames:
			geneNames.append(gn)

row = 0

writer = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/AllgeneNamesAppearedInDescriptions.xlsx")
worksheet = writer.add_worksheet()

for name in geneNames:
	for record in ahrdResult:
		words = record.split(" ")
		for w in words:	
		### check gene names
			if w == name: 
				worksheet.write(row,0,w)
				worksheet.write(row,1,record)

