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
def uniprotIdsExtraction(uniprotIdsFile, sprotFile, annotationFile): 

	referenceFile = open("/home/samaneh/eggNOG/referenceFile.fasta","w")
	for line in uniprotIdsFile.readlines()[1:]:
		uniprotId = line.split()[0]
		clusterNames = line.split()[1]
		for record in SeqIO.parse(sprotFile, "fasta"):
			sprotId = record.id.split("|")[1]
			if uniprotId == sprotId:
				newRecord = record
				for l in annotationFile.readlines():
					if uniprotId == l.split()[1]:
						description = l.split()[5]
						newRecord.description = description 
						SeqIO.write(newRecord, referenceFile, "fasta")

			

def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/data/uniprot-LUCA.tsv", "r")
	sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")
	annotationFile = open("/home/samaneh/eggNOG/data/NOG.annotations.tsv")
	uniprotIdDic = uniprotIdsExtraction(uniprotIdsFile, sprotFile,annotationFile)
	

if __name__ == "__main__":
	handler()





