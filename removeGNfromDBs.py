'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
from pandas import ExcelWriter

sprotDB = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))

dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"]

pattern = "GN="
geneList = []

geneNames = open("/home/samaneh/AHRD/outputs/sprotGeneNames.txt","w")

for dbSeq in SeqIO.parse(sprotDB, "fasta"):
	for token in dbSeq.description.split(" "):
		if pattern in token:
			geneName = token.strip(pattern)
			if geneName not in geneList:
				geneList.append(geneName)
				geneNames.write("\t")
				geneNames.write(geneName)

geneNames.close()

print "gene name list's length=", len(geneList)

#for record in ahrdResult:
#	for name in geneList:
#		if name in record:
#			print record
