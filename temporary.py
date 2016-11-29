'''
@auther: Samaneh

The whole planned algorithm is implemented here:


'''

from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os
import json

#########################################################################

uniprotIdsFile = open("/home/samaneh/eggNOG/data/other/uniprot-all.tsv", "r")
uniprotDict = dict()
tempList = []
newList = []
##@sam## extract a dictionary from cluster names as keys and uniprot ids as values


for line in uniprotIdsFile.readlines():
	clusterName = line.split()[0]
	#clusterNamesList.append(line.split()[0])
	uniprotId = line.split()[1].split(",") 
	if "-" in uniprotId:
		uniprotId.remove("-")
	if clusterName in uniprotDict.keys():
		tempList = uniprotDict[clusterName]
		newList = tempList + uniprotId
		uniprotDict.update({clusterName:newList})
	else:	
		uniprotDict.update({clusterName:uniprotId})
print uniprotDict
with open("/home/samaneh/eggNOG/uniprotIdsDictionary.json","w") as uniprotDicFile:
	json.dump(uniprotDict, uniprotDicFile)

uniprotDicFile.close()
print "done"
##################################

##@sam## exract the records related to each uniprot id from sprot: 

sprotDbFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta","r")

sprotIdsList = []
uniprotIdsList = []

sprotOutFile = open("/home/samaneh/eggNOG/sprotIncludedInEggnog.fasta","w")
descList = []

with open("/home/samaneh/eggNOG/clusteredDescriptions.txt","w") as f:
	for cluster in uniprotDict.keys():	##@sam## in each cluster name search all uniprot ids in sprot database, if it is found 
		newValueList = []
		for record in SeqIO.parse(sprotDbFile,"fasta"):
			sprotId = record.id.split("|")[1]
			for uid in uniprotDict[cluster]:
				if uid == sprotId:
					sprotIdList.append(record.id)
					des = record.description.strip(record.name).strip(" ")
					des = re.sub("OS=.*","",des)	
					descList.append(des)
		
		f.write("\n")
		f.write(cluster)
		for i in range(0,len(sprotIdsList)):
			f.write(sprotIdsList[i])
			f.write(" | ")
			f.write(descList[i])
		f.write("\n###############\n")





