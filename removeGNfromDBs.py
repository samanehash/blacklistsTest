'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter

sprotDB = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))

dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"]



pattern = "GN="
valueList = []
geneDic = dict()


for dbSeq in SeqIO.parse(sprotDB, "fasta"):				# parse sprot database fasta file
	for token in dbSeq.description.split(" "):			# each token of each description of database	
		if pattern in token:							# find the token containing gene name (GN=)
			if token.strip(pattern) == "putative":
				geneName = "al2"
			else:		
				geneName = token.strip(pattern)				# exclude GN= part of the mentioned token
			
			if geneName == "":							
				continue 
			#if geneName=="gene":						# in some descriptions format gene name is introduced as "GN=gene number
												
			else:				
				k = geneName[0]							# extract the first letter of token
				if k in geneDic.keys():
					valueList = list(geneDic.get(k))	# get the list of values (tokens) starting with letter in k
					if geneName not in valueList:	
						valueList.append(geneName)
						geneDic.update({k:valueList})
				else:
					geneDic.update({k:geneName})


appeared = dict()
row1 = 0

writer1 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/geneNamesAppearedInDescriptions.xlsx")
worksheet1 = writer1.add_worksheet()

writer2 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/geneNamesAppearedInDescriptions.xlsx")
worksheet2 = writer2.add_worksheet()

for record in ahrdResult:
	words = record.split(" ")
	for w in words:	
		# check homolog
		if w=="homolog":
			worksheet2.write(row2,0,record)
			row2 = row2 + 1
		# check gene names
		fLetter = w[0]
		if fLetter in geneDic.keys():
			for name in geneDic.get(fLetter):
				if w == name:
					if w not in appeared.keys():
						appeared.update({w:record})
						worksheet1.write(row1,0,w)
						worksheet1.write(row1,1,record)
						row1 = row1 + 1



