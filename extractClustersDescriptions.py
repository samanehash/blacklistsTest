'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re

##################################################################################

clstrFile = open("/home/samaneh/AHRD/clustering/uniprot_sprot_clusterd_70percents.clstr","r")
clstr = clstrFile.readlines()
seqIdDict = dict()
seqIdList = []
clstrNumber = "Null"
#tempWriter = xlsxwriter.Workbook("/home/samaneh/AHRD/clustering/clusters.xlsx")
#tempsheet = tempWriter.add_worksheet()
temprow = 0
tempFile = open("/home/samaneh/AHRD/clustering/clusters_70.txt","w")

for line in clstr:

	if ">Cluster" in line:
		if clstrNumber != "Null":
			seqIdDict[clstrNumber]=seqIdList
			#tempsheet.write(temprow,0,clstrNumber)
			#print clstrNumber
			l = len(seqIdList)
			#for i in range(1,l+1):
			#	tempsheet.write(temprow,i,seqIdList[i-1])	
			#temprow = temprow + 1
			#print seqIdList, "\n"
			for i in range (0,l):
				tempFile.write(seqIdList[i])
				tempFile.write(" ")
			tempFile.write("\n")
			seqIdList = [] 
		clstrNumber = re.sub("\>[A-Za-z]*\s","",line) 

	if ">sp|" in line:
		line = re.sub(".*>sp\|","",line)
		seqId = re.sub("\|.*","",line)
		seqId = seqId.strip("\n")
		seqIdList.append(seqId)	


#sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
#row = 0
#writer = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/clustersDescriptions.xlsx")
#worksheet = writer.add_worksheet()

#clusterList = []

#for record in SeqIO.parse(sprotFile, "fasta"):
#	for key in seqIdDict.keys():
#		for name in seqIdDict[key]:
#			if name in record.name:
#				print record.description
#				worksheet.write(row,0,key)
#				worksheet.write(row,1,record.description)
#				row = row + 1