'''
@auther: Samaneh

Extract swissprot ids from uniprot ids given by eggNOG


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
sprotDbFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta","r")

sprotIdsList = []
uniprotIdsList = []

sprotOutFile = open("/home/samaneh/eggNOG/sprotIncludedInEggnog.fasta","w")

for line in uniprotIdsFile.readlines():
	uniprotIdsList.append(line.split()[0])	
for record in SeqIO.parse(sprotDbFile,"fasta"):
	sprotId = record.id.split("|")[1]
	#sprotIdsList.append(record.id)
	for u in uniprotIdsList:
		if u == sprotId:
			SeqIO.write(record, sprotOutFile, "fasta")
			#print u, "####\n", record
sprotOutFile.close()			





