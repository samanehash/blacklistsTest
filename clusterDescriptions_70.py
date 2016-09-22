'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re

###########################################

clusterFile = open("/home/samaneh/AHRD/clustering/clusters_70.txt","r")

clusterDesc = open("/home/samaneh/AHRD/clustering/clusteredDescriptions_70.txt","w")

lines = clusterFile.readlines()
idList = []

sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"

for line in lines:
	words = line.split()
	idList.append(words)

tempList = [] 
for item in idList:
	if len(item)>2:
		tempList.append(item)

for i in range(0,len(tempList)):
	for name in tempList[i]:
		clusterDesc.write(name)
		clusterDesc.write("\t")
		for record in SeqIO.parse(sprotFile, "fasta"):
			if name in record.name:
				des = record.description.strip(record.name).strip(" ")
				des = re.sub("OS=.*","",des)		
				clusterDesc.write(des)
				clusterDesc.write("\n")
	clusterDesc.write("\n############\n")			



#for name in tempList[0]:
#	clusterDesc.write(name)
#	clusterDesc.write("\t")
#	for record in SeqIO.parse(sprotFile, "fasta"):
#		if name in record.name:
#			des = record.description.strip(record.name).strip(" ")
#			des = re.sub("OS=.*","",des)		
#			clusterDesc.write(des)
#			clusterDesc.write("\n")
#clusterDesc.write("\n############\n")


