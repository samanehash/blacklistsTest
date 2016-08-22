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

#geneNames = open("/home/samaneh/AHRD/outputs/sprotGeneNames.txt","w")

for dbSeq in SeqIO.parse(sprotDB, "fasta"):			# parse sprot database fasta file
	for token in dbSeq.description.split(" "):		# each token of each description of database	
		if pattern in token:						# find the token containing gene name (GN=)
			geneName = token.strip(pattern)			# exclude GN= part of the mentioned token
			if geneName == "":
				continue 
			#if geneName=="gene":					# in some descriptions format gene name is introduced as "GN=gene number
													# extract the first letter of token						
			else:
				k = geneName[0]
				#print "gene=", geneName, "\t", "first letter=", geneName[0]
				if k in geneDic.keys():
					valueList = list(geneDic.get(k))
					if geneName not in valueList:
						valueList.append(geneName)
						geneDic.update({k:valueList})
				else:
					geneDic.update({k:geneName})
#				geneNames.write("\t")
#				geneNames.write(geneName)

#geneNames.close()

#print "gene name list's length=", len(geneList)

appeared = dict()
row = 0

writer = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/geneNamesAppearedInDescriptions.xlsx")
worksheet = writer.add_worksheet()
for record in ahrdResult:
	#print record
	words = record.split(" ")
	for w in words:	
		fLetter = w[0]
		if fLetter in geneDic.keys():
			for name in geneDic.get(fLetter):
				if w == name:
					if w not in appeared.keys():
						appeared.update({w:record})
						worksheet.write(row,0,w)
						worksheet.write(row,1,record)
						row = row + 1
					#print record, "//and//", w 


print appeared
