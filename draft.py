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

def uniprotIdsExtraction(uniprotIdsFile):

	uniprotIdList = []
	for line in uniprotIdsFile.readlines()[1:]:
		uniprotId = line.split()[0]
		uniprotIdList.append(uniprotId)

	return uniprotIdList
		
def idsInSprotCheck(uniprotIdList, sprotFile):

	verifiedIdsList = []
	sprotDic = dict()
	for record in SeqIO.parse(sprotFile, "fasta"):
		sprotId = record.id.split("|")[1]
		for u in uniprotIdList:
			if sprotId == u:
				print sprotId
				verifiedIdsList.append(sprotId)
				desc = record.description.strip(record.name).lstrip(" ")
				desc = re.sub("OS=.*","",desc)
				sprotDic.update({sprotId:desc})

	return verifiedIdsList, sprotDic
	

def DescriptionExtraction(verifiedIdsList, sprotDic):


	idsDic = dict()
	descsDic = dict()
	clusterNamesList = []

	for uid in verifiedIdsList:
		for line in uniprotIdsFile.readlines()[1:]:
			if uid == line.split()[0]:
				desc = sprotDic[uid]
				print "type(desc)= ", type(desc)
				clusterNamesList = line.split()[1].split(",")
				for name in clusterNamesList:
					if name in idsDic.keys():
						##@sam## insert to ids dictionary
						idTempList = idsDic[name]
						idTempList.append(uid)
						idsDic.update({name:idTempList})
						##@sam## insert to descriptions dictionary
						descTempList = descsDic[name]
						descTempList.append(desc)
						descsDic.update({name:descTempList})

					else:
						##@sam## insert to ids dictionary
						uniprotList = []
						uniprotList.append(uid)
						idsDic.update({name:uniprotList})	
						##@sam## insert to descriptions dictionary
						descList = []
						descList.append(desc)
						descsDic.update({name:descList})
					
	writer(idsDic, descsDic)


def writer(clusterAndIdsDic, clusterAndDescsDic):

	clusteredFile = open("/home/samaneh/eggNOG/eggNOG_clusters_descriptions.txt","w")
	for cName in clusterAndIdsDic.keys():
		##@sam## the length of two lists below would be the same
		idsList = clusterAndIdsDic[cName]
		descsList = clusterAndDescsDic[cName]

		clusterName = cName + " :\n"
		clusteredFile.write(clusterName)
		
		for i in range(0,len(idsList)):
			line = idsList[i] + " | " + descList[i] + "\n"
			clusteredFile.write(line)

		clusteredFile("###################\n")	



def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/data/uniprot-LUCA.tsv", "r")
	uniprotIdList = uniprotIdsExtraction(uniprotIdsFile)
	sprotFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta", "r")
	verifiedIdsList, sprotDic = idsInSprotCheck(uniprotIdList, sprotFile)
	DescriptionExtraction(verifiedIdsList, sprotDic)
	



if __name__ == "__main__":
	handler()





