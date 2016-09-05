'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter

###extract list of geneNames from text file derived from uniprot
writer2 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/AllSprotGeneNames.xlsx")
row2 = 0

tokenFile = open("/home/samaneh/AHRD/outputs/TokenBlacklistIncGNs.txt","w") # create a new token blacklist including all swissprot gene names

geneNames = []
file = open("/home/samaneh/AHRD/data/uniprot-all.tab","r")
for line in file.readlines():
	if len(line.split())==3:
		gn = line.split()[2]
		if gn not in geneNames:
			geneNames.append(gn)
			worksheet2.write(row2,0,gn)
			row2 = row2 + 1
			tokenFile.write("^" + gn + "$" + "\n") # add unrepeated gene names into the new token blacklist

tokenFile.close()
