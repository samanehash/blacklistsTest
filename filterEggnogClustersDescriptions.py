'''
@auther: Samaneh

'''

from Bio import SeqIO
import pandas as pd
import numpy as np
#import xlsxwriter
import re
import csv
import os
import json

#######################################################################


def annotationExtraction(annotationFile):

	removeList = []
	for item in annotationFile.readlines():
		clusterName = item.split("\t")[1].strip()
		desc = item.split("\t")[5].strip()
		if desc == "NA":
			removeList.append(clusterName)		
	return removeList

def filtering(removeList, clusteredFile):

	resFile = open("/home/samaneh/eggNOG/output/eggNOG_clustering_descriptions_filtered.txt", "w")
	dual = dict()

	for line in clusteredFile.readlines():

		if " :" in line :
			##@sam##	clear all dictionary and list and cluaterName variables for next cluster storage
			dual.clear()
			clusterName = re.sub(":","",line)
			clusterName = clusterName.strip("\n").strip(" ")

		elif "|" in line:
			uniprotId = line.split("|")[0].rstrip(" ")
			desc = line.split("|")[1].strip(" ")
			dual.update({uniprotId:desc})
			#print idList

		elif "#" in line:
			if clusterName not in removeList:	
				##@sam##	write into the file
				toPrint = clusterName + " :\n"
				for n in dual.keys():
					toPrint = toPrint + ">>" + n + " | " + dual[n]
				toPrint = toPrint + "\n############" + "\n"	 	
				resFile.write(toPrint)

		else:
			continue

	resFile.close()	


def handler():

	annotationFile = open("/home/samaneh/eggNOG/data/NOG.annotations.tsv", "r")
	removeList = annotationExtraction(annotationFile)
	clusteredFile = open("/home/samaneh/eggNOG/output/eggNOG_clustering_descriptions.txt","r")
	filtering(removeList, clusteredFile)
	

if __name__ == "__main__":
	handler()

		


