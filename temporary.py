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

def extraction(uniprotIdsFile, sprotFile):


	idsDic = dict()
	descsDic = dict()
	clusterNamesList = []

	for line in uniprotIdsFile.readlines()[1:]:
		uniprotId = line.split()[0]
		for record in SeqIO.parse(sprotFile, "fasta"):
			sprotId = record.id.split("|")[1]
			if sprotId == uniprotId :
				print uniprotId
				desc = record.description.strip(record.name).lstrip(" ")
				desc = re.sub("OS=.*","",desc)

				clusterNamesList = line.split()[1].split(",")
				for name in clusterNamesList:
					if name in idsDic.keys():
						##@sam## insert to ids dictionary
						idTempList = idsDic[name]
						idTempList.append(uniprotId)
						idsDic.update({name:idTempList})
						##@sam## insert to descriptions dictionary
						descTempList = descsDic[name]
						descTempList.append(desc)
						descsDic.update({name:descTempList})

					else:
						##@sam## insert to ids dictionary
						uniprotList = []
						uniprotList.append(uniprotId)
						idsDic.update({name:uniprotList})	
						##@sam## insert to descriptions dictionary
						descList = []
						descList.append(desc)
						descsDic.update({name:descList})

	print idsDic, descsDic					
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
	sprotFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta", "r")
	extraction(uniprotIdsFile, sprotFile)



if __name__ == "__main__":
	handler()





