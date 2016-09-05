'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
##########################################################################

ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_sprot3_newTokenBlacklist.xlsx"))
dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"]


###extract list of geneNames from text file derived from uniprot
writer2 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/AllSprotGeneNames.xlsx")
worksheet2 = writer2.add_worksheet()
row2 = 0

geneNames = []
file = open("/home/samaneh/AHRD/data/uniprot-all.tab","r")
for line in file.readlines():
	if len(line.split())==3:
		gn = line.split()[2]
		if gn not in geneNames:
			geneNames.append(gn)
			worksheet2.write(row2,0,gn)
			row2 = row2 + 1

