'''
@auther: Samaneh

WORKING VERSION

from eggnog clusters data the cluster names, eggnog specified sequences' IDs (NOG.members.tsv), 
all aligned sequences of each cluster (NOG_raw_algs), and the representative description (selected
by eggnog algorithm) for each cluster (NOG.annotations.tsv) are available.

Here I am 1. diminishing the clusters to only those cluster with sequences present in sprot
database be included -> next script: 2. select the representative description for remaining clusters using my 
algorithm 


'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os

######################################################

members = open("/home/samaneh/eggNOG/data/NOG.members.tsv","r")
clusterNameList = []
for member in members:
	member = member.strip().split("\t")
	clusterNameList.append(member[0] + "." + member[1])  ##@sam## a list of cluster names should be extracted from member file
	#memberNames = member[-1].split(",")
	#clustersDic.update({clusterName:memberNames})

dbFile = open("/home/samaneh/AHRD/data/uniprot_sprot.fasta")

clustersDic = dict()
namesList = []
seqdescs = []
seqList = []
desList = []

for cluster in clusterNameList:			##@sam## phase2,3
	fileToOpen = "/home/samaneh/eggNOG/data/NOG_raw_algs/" + cluster   ##@sam## according to the clusterName generate the name of cluster's
	suffixList = [".meta_raw.fa", ".meta_raw.fasta", ".clustalo_raw.fa", ".mafft_raw.fa"]	##@sam## gives us 190637 out of 190649 so far
	for s in suffixList:
		fileToOpenName = fileToOpen + s 									##@sam## fasta file to be retrieved from raw_alg address
		if os.path.isfile(fileToOpenName):	##@sam## checks if such file exists
			clusterFile = open((fileToOpenName),"r")
			namesList.append(cluster)
	seqNumber = 0
	count = 0		
	for record in SeqIO.parse(clusterFile, "fasta"):
		seqNumber = seqNumber + 1
		sequence = str(record.seq).replace("-","")
		for entry in SeqIO.parse(dbFile, "fasta"):
			if sequence == entry.seq:
				#seqList.append(sequence)
				desList.append(entry.description)
				print entry.description
				count = count + 1
	if 	seqNumber == count:
		clustersDic.update({cluster:desList})		
	
clusterDictionaryFile = open("/home/samaneh/eggNOG/clusterDictionary","w")
for k in clustersDic.keys():
	clusterDictionaryFile.write(k)
	#print clustersDic[k]
	for v in clustersDic[k]:
		clusterDictionaryFile.write(v)
	clusterDictionaryFile.write("###########")



