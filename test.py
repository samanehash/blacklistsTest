'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
from multiprocessing import Pool

###########################################

def prepareNamesList(clusterNamesFile):

	idList = []
	lines = clusterNamesFile.readlines()
	for line in lines:
		words = line.split()
		idList.append(words)

	namesList = [] 
	for item in idList:
		if len(item)>2:
			namesList.append(item)

def writingNames(indx):

	sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
	clusterDesc = open("/home/samaneh/AHRD/clustering/clusteredDescriptions.txt","w")
	for name in namesList[indx]:
		clusterDesc.write(name)
		clusterDesc.write("\t")
		for record in SeqIO.parse(sprotFile, "fasta"):
			if name in record.name:
				des = record.description.strip(record.name).strip(" ")
				des = re.sub("OS=.*","",des)		
				clusterDesc.write(des)
				clusterDesc.write("\n")
	clusterDesc.write("\n############\n")

def main():
	clusterFile = open("/home/samaneh/AHRD/clustering/clusters.txt","r")
	prepareNamesList(clusterFile)
			
	for i in range (0, len(namesList)):
		p = Pool(i)
		p.writingNames(i)

if __name__ == "__main__": 		
	main()						 








