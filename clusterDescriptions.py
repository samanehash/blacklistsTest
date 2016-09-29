'''
@auther: Samaneh

This module extract the descriptions of each sequence of clusters containing more than two members
into a text file

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import multiprocessing
from multiprocessing.dummy import Pool
import time

###########################################

### generate a list whose each item is a list of all names in a cluster>1
def prepareName(clusterFile):

	lines = clusterFile.readlines()

	namesList = []
	for line in lines:
		words = line.split()
		if len(words)>1:
			namesList.append(words)

	return namesList

### extract the descriptions related to each name of cluster from sprot database file
def writingNames(namesList, indx):
	selDesList = []
	sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot_filteredForClustering.fasta"
	for name in namesList[indx]:
		#print name
		selDes = ""
		selDes += name
		selDes += "\t"
		for record in SeqIO.parse(sprotFile, "fasta"):
			if name in record.name:
				des = record.description.strip(record.name).strip(" ")
				des = re.sub("OS=.*","",des)
				selDes += des
				selDes += "\n"		
		selDesList.append(selDes)
	return selDesList	

def handler():

### call prepareNamesList function
	clusterFile = open("/home/samaneh/AHRD/clustering/clusters.txt","r")
	namesList = prepareName(clusterFile)

#p = Pool(4)
### to check CPU band you can use: multiprocessing.cpu_count()
### result here shows 4 then it also make sense to use pool(4)
### however there is no limitation for pool and the limitation 

### will be put on by CPU itself
	rng = range(0, len(namesList))

### call writingNames dunction and write the extracted descriptions into a file	
	with open("/home/samaneh/AHRD/clustering/clusteredDescriptions_multiprocessed.txt","w") as f:
		for result in (writingNames(namesList, i) for i in rng):
			for n in result: 
				f.write(n)
			f.write("\n############\n")

if __name__ == "__main__":
	handler()
