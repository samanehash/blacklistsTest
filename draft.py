'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re

###########################################

clusterFile = open("/home/samaneh/AHRD/clustering/clusters.txt","r")

clusterDesc = open("/home/samaneh/AHRD/clustering/clusteredDescriptions.txt","w")

lines = clusterFile.readlines()
idList = []

for line in lines:
	words = line.split()
	idList.append(words)

sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"

for item in idList:
	if len(item)>1:
		for name in item:
			for record in SeqIO.parse(sprotFile, "fasta"):
				if name == record.name:
					clusterDesc.write(record.description)
					clusterDesc.write("\n")
		clusterDesc.write("###")
		clusterDesc.write("\n")			
#		for name in seqIdDict[key]:
#			if name in record.name:
#				print record.description
#				worksheet.write(row,0,key)
#				worksheet.write(row,1,record.description)
#				row = row + 1


