'''
@auther: Samaneh

WORKING VERSION

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os

######################################################

members = open("/home/samaneh/eggNOG/data/eukaryotes/euNOG.members.tsv","r")
clusterNameList = []
for member in members:
	member = member.strip().split("\t")
	clusterNameList.append(member[0] + "." + member[1])  ##@sam## a list of cluster names should be extracted from member file
	#memberNames = member[-1].split(",")
	#clustersDic.update({clusterName:memberNames})

#print clustersDic
clustersDic = dict()
seqdescs = desList = []
dbFile = open("/home/samaneh/AHRD/data/uniprot_trembl.fasta")
count = 0
for cluster in clusterNameList:			##@sam## phase2,3
	fileToOpen = "/home/samaneh/eggNOG/data/eukaryotes/euNOG_raw_algs/" + cluster   ##@sam## according to the clusterName generate the name of cluster's
	fileToOpenName = fileToOpen + ".meta_raw.fa" 									##@sam## fasta file to be retrieved from raw_alg address
	if os.path.isfile(fileToOpenName):
		clusterFile = open((fileToOpenName),"r")
	else:
		fileToOpenName = fileToOpen + ".clustalo_raw.fa"
		if os.path.isfile(fileToOpenName):
			clusterFile = open((fileToOpenName),"r")
		else:	
			fileToOpenName = fileToOpen + ".mafft_raw.fa"
			clusterFile = open((fileToOpenName),"r")	
	for record in SeqIO.parse(clusterFile, "fasta"):
		desList.append(str(record.seq).replace("-",""))		
	for seq in SeqIO.parse(dbFile, "fasta"):		##@sam## from each cluster's fasta file the sequences of memebers can be rerived	
		for des in desList:							##@sam## and be compared with all sequences of trembl. when the matched sequences are found,
			if des == str(seq.seq):					##@sam## the descriptions will be extracted and added as values of coresponding key(cluster name)
				seqdescs.append(seq.description)
	clustersDic.update({cluster:seqdescs})			
print clustersDic
clusterDictionaryFile = open("/home/samaneh/eggNOG/clusterDictionary","w")
for k in clustersDic.keys():
	clusterDictionaryFile.write(k)
	#print clustersDic[k]
	clusterDictionaryFile.write(clustersDic[k])
	clusterDictionaryFile.write("###########")

#print members.readlines()[0].strip().split("\t")[-1].split(",")






