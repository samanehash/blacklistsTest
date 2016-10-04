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

class cluster():

	namesList = []
	selDesList = []

### generate a list whose each item is a list of all names in a cluster>1
	def prepareName(self, clusterFile):

		lines = clusterFile.readlines()
		for line in lines:
			words = line.split()
			if len(words)>1:
				self.namesList.append(words)

### extract the descriptions related to each name of cluster from sprot database file
	def writingNames(self,idnx):
		self.selDesList = []
		sprotFile = "/home/samaneh/AHRD/data/db/uniprot_sprot_filteredForClustering.fasta"

		for name in self.namesList[idnx]:
			selDes = ""
			selDes += name
			selDes += " "
			selDes += "| "
			for record in SeqIO.parse(sprotFile, "fasta"):
				if name in record.name:
					des = record.description.strip(record.name).strip(" ")
					des = re.sub("OS=.*","",des)
					selDes += des
					selDes += "\n"	

			self.selDesList.append(selDes)	

def handler():
	n = cluster()
	clusterFile = open("/home/samaneh/AHRD/clustering/clusters.txt","r")
	n.prepareName(clusterFile)
	with open("/home/samaneh/AHRD/clustering/clusteredDescriptions_final.txt","w") as f:
		for i in range(0, len(n.namesList)):
			n.writingNames(i)
			for item in n.selDesList:
				f.write(item)
			f.write("\n############\n")		



if __name__ == "__main__":
	
	handler()
