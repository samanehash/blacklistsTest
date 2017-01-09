'''
@auther: Samaneh


'''

from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os
import json
############################################################################################

##@sam## Find the intersection between eggNOG and swissprot: return a list of corresponding ids

def bothIdsExtraction(sprotFile,uniprotIdsFile):
	uniprotList = []
	sprotList = []
	idsDict = dict()
	descsDict = dict()

	for record in SeqIO.parse(sprotFile, "fasta"):
		sprotId = record.id.split("|")[1]
		sprotList.append(sprotId)

		sprotDisc = record.description.strip(record.name).lstrip(" ")
		sprotDisc = re.sub("OS=.*","",sprotDisc)
		descsDict.update({sprotId:sprotDisc})
		

	for line in uniprotIdsFile:
		uniprotId = line.split()[0].strip(" ")
		uniprotList.append(uniprotId)
		uniprotClusters = line.split()[1].split(",")
		idsDict.update({uniprotId:uniprotClusters})

	bothIdsList = set(sprotList).intersection(set(uniprotList))	

	for d in idsDict.keys():
		if d not in bothIdsList:
			del idsDict[d]
	for de in descsDict.keys():
		if de not in bothIdsList:
			del descsDict[de] 		

	return idsDict, descsDict

####################################

def DescriptionExtraction(idsDict, descsDict):

	idsDic = dict()
	descsDic = dict()

	for i in idsDict.keys():
		clusters = idsDict[i]
		for cluster in clusters:
			if cluster in idsDic.keys():
				##@sam## insert to ids dictionary
				idTempList = idsDic[cluster]
				idTempList.append(i)
				idsDic.update({cluster:idTempList})

				##@sam## insert to descriptions dictionary
				descTempList = descsDic[cluster]
				descTempList.append(descsDict[i])
				descsDic.update({cluster:descTempList})
			else:
				##@sam## insert to ids dictionary
				idList = []
				idList.append(i)
				idsDic.update({cluster:idList})

				##@sam## insert to descriptions dictionary
				descList = []
				descList.append(descsDict[i])
				descsDic.update({cluster:descList})

		
	writer(idsDic, descsDic)

def writer(clusterAndIdsDic, clusterAndDescsDic):

	clusteredFile = open("/home/samaneh/eggNOG/output/eggNOG_clustering_descriptions_all.txt","w")
	for cName in clusterAndIdsDic.keys():
		##@sam## the length of two lists below would be the same
		idsList = clusterAndIdsDic[cName]
		descsList = clusterAndDescsDic[cName]

		clusterName = cName + " :\n"
		clusteredFile.write(clusterName)
		
		for i in range(0,len(idsList)):
			line = idsList[i] + " | " + descsList[i] + "\n"
			clusteredFile.write(line)

		clusteredFile.write("\n###################\n")	

	clusteredFile.close()	

def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/data/uniprot-LUCA.tsv", "r")
	sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")

	idsDict, descsDict = bothIdsExtraction(sprotFile, uniprotIdsFile)
	uniprotIdDic = DescriptionExtraction(idsDict, descsDict)
	

if __name__ == "__main__":
	handler()	