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
######################################################


def scanFile(clusterDescriptionsFile):

	flag = False
	newSprotFile = open("/home/samaneh/eggNOG/output/representative_uniprot_sprot.fasta","w")
	for line in clusterDescriptionsFile:
		if " :" in line:
			#if "ENOG41121DW" in line:
			#	flag = True
			idsList = []
		elif ">>" in line:
			idsList.append(line.split("|")[0].lstrip(">>").strip(" "))
			#if flag == True:
			#	inspector = line
			#	flag = False
		elif "*" in line:
			#if idsList == []:
			#	print inspector
			rec = generateDBfile(idsList)
			SeqIO.write(rec, newSprotFile, "fasta")



def generateDBfile(idsList):

	sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")
	keepRecord = open("/home/samaneh/eggNOG/output/temp.fasta","w")
	idSeqDict = dict()
	idRecordDict = dict()
	for record in SeqIO.parse(sprotFile, "fasta"):
		ac = record.id.split("|")[1]
		if ac in idsList:
			idSeqDict.update({ac:record.seq})
			#savedRecord = SeqIO(record.seq, id=record.id, name=record.name, description=record.description, dbxrefs=None, features=None, annotations=None, letter_annotations=None)
			SeqIO.write(record,keepRecord,"fasta")	
	representativeId = selectSeq(idSeqDict)
	keepRecord = open("/home/samaneh/eggNOG/output/temp.fasta","r")
	for rec in SeqIO.parse(keepRecord,"fasta"):
		if rec.id.split("|")[1] == representativeId:
			return rec
	

	#representativeRecord = [rec if rec.id.split("|")[0] == representativeId for rec in SeqIO.parse(keepRecord,"fasta")]
	


def selectSeq(idSeqDict):

	comparisonList = idSeqDict.values()
	longestSeq = max(comparisonList, key=len)
	for k,v in idSeqDict.items():
		if v == longestSeq:
			representativeId = k

	return representativeId			


def handler():

	clusterDescriptionsFile = open("/home/samaneh/eggNOG/output/ClusterDescriptions_onEggNOG_all.txt","r")
	scanFile(clusterDescriptionsFile)




if __name__ == "__main__":
	handler()

