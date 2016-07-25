'''
@auther: Samaneh

'''
from Bio import SeqIO
from pandas import ExcelWriter
import numpy as np
import pandas as pd

#sprot
SprotRef1 = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_3_references.fasta"
SprotRef2 = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_4_references.fasta"

#Tair
TairRef1 = "/home/samaneh/AHRD/data/reference/nrTair/non_red_tair10_batch_1_references.fasta"
TairRef2 = "/home/samaneh/AHRD/data/reference/nrTair/non_red_tair10_batch_2_references.fasta"

#Blumeria
BlumeriaRef = "/home/samaneh/AHRD/data/reference/blumeria_graminis_references.fasta"

des_blacklist = open("/home/samaneh/AHRD/data/blacklist_descline.txt", "r")
blacklist = des_blacklist.readlines()

refFiltered = ExcelWriter("/home/samaneh/AHRD/outputs/5references_filtered.xlsx")

desList = []
sprotFilteredList = []
tairFilteredList = []
blumeriaFilteredList = []
sprotRecList = []
tairRecList = []
blumeriaRecList = []

for token in blacklist:
	desList.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))
recList = []

for record in SeqIO.parse(SprotRef1, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				sprotRecList.append(record.id)
				newRec = (record.description).strip(record.name).strip(" ")
				if newRec not in sprotFilteredList: 	
					sprotFilteredList.append(newRec)


for record in SeqIO.parse(SprotRef2, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				sprotRecList.append(record.id)
				newRec = (record.description).strip(record.name).strip(" ")
				if newRec not in sprotFilteredList: 	
					sprotFilteredList.append(newRec)


for record in SeqIO.parse(TairRef1, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():			
			if record.id not in recList:
				tairRecList.append(record.id)
				newRec = (record.description).strip(record.name).strip("| Symbols: |")
				if newRec not in tairFilteredList: 	
					tairFilteredList.append(newRec)


for record in SeqIO.parse(TairRef2, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				tairRecList.append(record.id)
				newRec = (record.description).strip(record.name).strip("| Symbols: |")
				if newRec not in tairFilteredList: 	
					tairFilteredList.append(newRec)


for record in SeqIO.parse(BlumeriaRef, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				blumeriaRecList.append(record.id)
				newRec = (record.description).strip(record.name).strip(" ")
				if newRec not in blumeriaFilteredList: 	
					blumeriaFilteredList.append(newRec)


sprotFilteredDf = pd.DataFrame(sprotFilteredList)
sprotFilteredDf.to_excel(refFiltered, "sprot")

tairFilteredDf = pd.DataFrame(tairFilteredList)
tairFilteredDf.to_excel(refFiltered, "tair")

blumeriaFilteredDf = pd.DataFrame(blumeriaFilteredList) 				
blumeriaFilteredDf.to_excel(refFiltered, "blumeria")

refFiltered.save()
