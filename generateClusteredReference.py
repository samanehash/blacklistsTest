'''
@auther: Samaneh
The whole planned algorithm is implemented here:
'''

from Bio import SeqIO
import pandas as pd
import numpy as np
#import xlsxwriter
import re
import csv
import os
import json

#########################################################################

##@sam## 	Extracts all the uniprot IDs and corresponding clusters from eggNOG tsv file into a dictionary
def uniprotIdsExtraction(uniprotIdsFile): 

	idsList = []
	idDesDic = dict()

	for line in uniprotIdsFile.readlines():
		if ">>" in line:
			ids = line.split("|")[0]
			ids = re.sub(">>","",ids).strip(" ")
			desc = line.split("|")[1].lstrip(" ")
			if ids not in idDesDic.keys():
				idDesDic.update({ids:desc})	
			else:
				newDesc = idDesDic[ids] + " / " + desc 
				idDesDic.update({ids:newDesc})			

	return idDesDic


def referenceGenerator(idDesDic, sprotFile):

	reference = open("/home/samaneh/eggNOG/output/clstrd_ref_eggNOG_descs.fasta", "w")
	for record in SeqIO.parse(sprotFile, "fasta"):
		spId = record.id.split("|")[1]
		if spId in idDesDic.keys():
			newRecord = record
			newRecord.description = idDesDic[spId] 
			SeqIO.write(newRecord, reference, "fasta")

	reference.close()			
		

def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/output/eggnogClusterDescriptions_onEggNOG.txt", "r")
	sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")

	idDesDic = uniprotIdsExtraction(uniprotIdsFile)
	referenceGenerator(idDesDic, sprotFile)
	

if __name__ == "__main__":
	handler()

