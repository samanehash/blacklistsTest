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

#################################################################################

def extraction(filteredClusters):

	idList = []
	for line in filteredClusters.readlines():
		if ">>" in line:
			idList.append(line.split("|")[0].lstrip(">>").rstrip(" "))
	return idList

def descriptionExtraction(annotationFile):


	descsDic = dict()
	for item in annotationFile.readlines():
		clusterName = item.split("\t")[1].strip()
		desc = item.split("\t")[5].strip()
		descsDic.update({clusterName:desc})	
 	
	return descsDic


def generate(filteredDescs, descsDic ,idList):

	resFile = open("/home/samaneh/eggNOG/output/eggnogClusterDescriptions_onEggNOG.txt", "w")
	dualDic = dict()

	for line in filteredDescs.readlines():
		if " :" in line :
			##@sam##	clear all dictionary and list and cluaterName variables for next cluster storage
			dualDic.clear()
			clusterName = ""

		  	clusterName = re.sub(" :","",line).strip(" ")
			clusterName = clusterName.strip("\n").strip(" ")

		elif ">>" in line:
			dual = line.split("|")
			uniprotId = dual[0].lstrip(">>").rstrip(" ")
			if uniprotId in idList:
				desc = descsDic[clusterName]
				dualDic.update({uniprotId:desc})

		elif "#" in line:
			##@sam##	write into the file
			toPrint = clusterName + " :\n"
			for n in dualDic.keys():
				toPrint = toPrint + ">>" + n + " | " + dualDic[n] + "\n"
			toPrint = toPrint + "\n**************" + "\n"	 	
			resFile.write(toPrint)

		else:
			continue

	resFile.close()								



def handler():

	filteredDescs = open("/home/samaneh/eggNOG/output/eggNOG_clustering_descriptions_filtered.txt")
	filteredClusters = open("/home/samaneh/eggNOG/output/ClusterDescriptions_onEggNOG.txt")
	annotationFile = open("/home/samaneh/eggNOG/data/NOG.annotations.tsv", "r")

	idList = extraction(filteredClusters)
	descsDic = descriptionExtraction(annotationFile)
	generate(filteredDescs, descsDic, idList)


if __name__ == "__main__":
	handler()





