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