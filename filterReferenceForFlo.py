'''
@auther: Samaneh

'''

from Bio import SeqIO
from pandas import ExcelWriter
import numpy as np
import pandas as pd



desList_sprot = []

sprotRecList_batch1 = []
sprotRecList_batch2 = []


###sprot reference filtering
SprotRef_batch1 = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_1_references.fasta"
SprotRef_batch2 = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_2_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklists/blacklist_descline_sprot.txt", "r")
blacklist_sprot = des_blacklist.readlines()

for token in blacklist_sprot:
	desList_sprot.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))


#sprot_batch1 filtering
for record in SeqIO.parse(SprotRef_batch1, "fasta"):
	for token in desList_sprot:
		if token.lower() in record.description.lower():
			if record.id not in sprotRecList_batch1:
				sprotRecList_batch1.append(record.id) # save the sequence id which CONTAINS blacklist tokens


#sprot_batch2 filtering
for record in SeqIO.parse(SprotRef_batch2, "fasta"):
	for token in desList_sprot:
		if token.lower() in record.description.lower():
			if record.id not in sprotRecList_batch2:
				sprotRecList_batch2.append(record.id) # save the sequence id which CONTAINS blacklist tokens


#############################################################################################
#### generate two new reference sets for each set ####

sprotRefFiltered_batch1 = open("/home/samaneh/AHRD/data/reference/sprot_batch_1_reference_filtered.fasta","w")	
sprotRefincBlacklist_batch1 = open("/home/samaneh/AHRD/data/reference/sprot_batch_1_reference_incBlacklist.fasta","w") # CONTAINS blacklist tokens

sprotRefFiltered_batch2 = open("/home/samaneh/AHRD/data/reference/sprot_batch_2_reference_filtered.fasta","w")	
sprotRefincBlacklist_batch2 = open("/home/samaneh/AHRD/data/reference/sprot_batch_2_reference_incBlacklist.fasta","w") # CONTAINS blacklist tokens

for record in SeqIO.parse(SprotRef_batch1, "fasta"):
	if record.id in sprotRecList_batch1:		
		SeqIO.write(record, sprotRefincBlacklist_batch1, "fasta")
	else:	
 		SeqIO.write(record, sprotRefFiltered_batch1, "fasta")
 		#if record.id not in sprotFilteredList_batch1:
 		#	sprotFilteredList_batch1.append(record.id)

for record in SeqIO.parse(SprotRef_batch2, "fasta"):
	if record.id in sprotRecList_batch2:		
		SeqIO.write(record, sprotRefincBlacklist_batch2, "fasta")
	else:	
 		SeqIO.write(record, sprotRefFiltered_batch2, "fasta")
 		#if record.id not in sprotFilteredList:
 		#	tairFilteredList.append(record.id)

sprotRefFiltered_batch1.close()
sprotRefincBlacklist_batch1.close()
sprotRefFiltered_batch2.close()
sprotRefincBlacklist_batch2.close()


