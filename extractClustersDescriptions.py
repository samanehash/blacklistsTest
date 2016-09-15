'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re

##################################################################################

clstrFile = open("/home/samaneh/AHRD/clustering/uniprot_sprot_clusterd.clstr","r")
clstr = clstrFile.readlines()
seqIdDict = dict()
seqIdList = []
clstrNumber = "Null"

for line in clstr:

	if ">Cluster" in line:
		if clstrNumber != "Null":
			seqIdDict[clstrNumber]=seqIdList
			seqIdList = [] 
		clstrNumber = re.sub("\>[A-Za-z]*\s","",line) 

	if ">sp|" in line:
		line = re.sub(".*>sp\|","",line)
		seqId = re.sub("\|.*","",line)
		seqIdList.append(seqId)

tremblInFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
row = 0
writer = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/clustersDescriptions.xlsx")
worksheet = writer.add_worksheet()

clusterList = []

for record in SeqIO.parse(tremblInFile, "fasta"):
	for key in seqIdDict.keys():
		for name in seqIdDict[key]:
			if name in record.name:
				print record.description
				worksheet.write(row,0,key)
				worksheet.write(row,1,record.description)
				row = row + 1