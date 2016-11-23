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

#########################################################################

uniprotIdsFile = open("/home/samaneh/eggNOG/data/other/uniprot-all.tsv", "r")
uniprotDict = dict()

##@sam## extract a dictionary from cluster names as keys and uniprot ids as values

for line in uniprotIdsFile.readlines():
	clusterId = line.split()[1].split(",")
	uniprotId = list(line.split()[0])
	for c in clusterId:               
		if c in uniprotDict.keys():
			tempList = uniprotDict[c]
			tempList.append(uniprotId)
			uniprotDict.update({c:tempList})
		else:	
			uniprotDict.update({c:uniprotId})

uniprotDicFile = open("/home/samaneh/essNOG/uniprotIdsDictionary.json","w")
uniprotDicFile.write(uniprotDict)
print "done"
##################################

##@sam## exract the records related to each uniprot id from sprot: 

sprotDbFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta","r")

sprotIdsList = []
uniprotIdsList = []

sprotOutFile = open("/home/samaneh/eggNOG/sprotIncludedInEggnog.fasta","w")
descList = []

for k in uniprotDict.keys():	##@sam## in each cluster name search all uniprot ids in sprot database, if it is found 
	newValueList = []
	for record in SeqIO.parse(sprotDbFile,"fasta"):
		sprotId = record.id.split("|")[1]
		for u in uniprotDict[k]:
			if u == sprotId:
				newValueList.append(record.id)
				des = record.description.strip(record.name).strip(" ")
				des = re.sub("OS=.*","",des)	
				descList.append(des)
	uniprotDict.update({k:newValueList}) 	##@sam## updates the dictionary in a way that includes only uniprot id that are included in sprot
with open("/home/samaneh/eggNOG/clusteredDescriptions.txt","w") as f:
	for item in descList:
		f.write(item)
	f.write("\n############\n")		




print uniprotDict

##@sam## create a descriptions file like what clusterDescriptions.py creates




