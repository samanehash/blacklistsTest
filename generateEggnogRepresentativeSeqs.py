'''
@auther: Samaneh


'''

from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os
import json

##################################################################################

##@sam## Find the intersection between eggNOG and swissprot: return a list of corresponding ids

def bothIdsExtraction(sprotFile, tremblFile, uniprotIdsFile):
	uniprotList = []
	sprotList = []
	tremblList = []
	idsDict = dict()
	sDescsDict = dict()
	tDescsDict = dict()
	unionDict = dict()

	for line in uniprotIdsFile:
		uniprotId = line.split()[0].strip(" ")
		uniprotList.append(uniprotId)
		uniprotClusters = line.split()[1].split(",")
		idsDict.update({uniprotId:uniprotClusters})
	print "uniprot list", len(uniprotList) , "\n"	

	for record in SeqIO.parse(sprotFile, "fasta"):
		sprotId = record.id.split("|")[1]
		sprotList.append(sprotId)
		sprotDisc = record.description.strip(record.name).lstrip(" ")
		sprotDisc = re.sub("OS=.*","",sprotDisc)
		sDescsDict.update({sprotId:sprotDisc})

	sprotIntrsctIdsList = set(sprotList).intersection(set(uniprotList))	
	print "sprot list", len(sprotIntrsctIdsList), "\n"

	for record in SeqIO.parse(tremblFile, "fasta"):
		tremblId = record.id.split("|")[1]
		tremblList.append(tremblId)
		tremblDisc = record.description.strip(record.name).lstrip(" ")
		tremblDisc = re.sub("OS=.*","",tremblDisc)
		tDescsDict.update({tremblId:tremblDisc})	
		
	tremblIntrsctIdsList = set(tremblList).intersection(set(uniprotList))
	print "trembl list", len(tremblIntrsctIdsList), "\n"

	for k in sDescsDict.keys():
		if k not in sprotIntrsctIdsList:
			del sDescsDict[k]
	for ke in tDescsDict.keys():
		if ke not in tremblIntrsctIdsList:
			del tDescsDict[ke] 		

	unionDict = sDescsDict.copy()
	unionDict.update(tDescsDict)
	print "union dictionary keys", len(unionDict.keys()), "\n"		
	#return idsDict, descsDict

####################################


def handler():

	uniprotIdsFile = open("/home/samaneh/eggNOG/data/uniprot-LUCA.tsv", "r")
	sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")
	tremblFile = open("/home/samaneh/AHRD/data/db/uniprot_trembl.fasta", "r")

	bothIdsExtraction(sprotFile, tremblFile, uniprotIdsFile)
	
	

if __name__ == "__main__":
	handler()	


















