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

##@sam## 	Extracts all the uniprot IDs and corresponding clusters from eggNOG tsv file into a dictionary
def uniprotIdsExtraction(uniprotIdsFile): 

	uniprotIdDic = dict()
	for line in uniprotIdsFile.readlines()[1:]:
		uniprotId = line.split()[0]
		uniprotClusters = line.split()[1].split(",")
		uniprotIdDic.update({uniprotId:uniprotClusters})
	
	return uniprotIdDic
		

##@sam##	checkes the existance of uniprots in swissprot and for those that are included in sprot generates
#			two dictionaries with clusternames as keys and one with sprot(uniprot) ids as values and the other
#			one with sprot descriptions as values  					
def DescriptionExtraction(uniprotIdDic, sprotFile):

	idsDic = dict()
	descsDic = dict()

	for record in SeqIO.parse(sprotFile, "fasta"):
		sprotId = record.id.split("|")[1]
		for u in uniprotIdDic.keys():
			if sprotId == u:
				desc = record.description.strip(record.name).lstrip(" ")
				desc = re.sub("OS=.*","",desc)
				for clusterName in uniprotIdDic[u]:
					if clusterName in idsDic.keys():
						##@sam## insert to ids dictionary
						idTempList = idsDic[clusterName]
						idTempList.append(u)
						idsDic.update({clusterName:idTempList})
						##@sam## insert to descriptions dictionary
						descTempList = descsDic[clusterName]
						descTempList.append(desc)
						descsDic.update({clusterName:descTempList})

					else:
						##@sam## insert to ids dictionary
						uniprotList = []
						uniprotList.append(u)
						idsDic.update({clusterName:uniprotList})	
						##@sam## insert to descriptions dictionary
						descList = []
						descList.append(desc)
						descsDic.update({clusterName:descList})


	print idsDic, descsDic			
	writer(idsDic, descsDic)



def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/data/uniprot-LUCA.tsv", "r")
	uniprotIdDic = uniprotIdsExtraction(uniprotIdsFile)
	sprotFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta", "r")
	DescriptionExtraction(uniprotIdDic, sprotFile)
	



if __name__ == "__main__":
	handler()





