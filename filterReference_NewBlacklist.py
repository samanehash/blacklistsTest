'''
@auther: Samaneh

'''

from Bio import SeqIO
from pandas import ExcelWriter
import numpy as np
import pandas as pd



desList_sprot = []
desList_tair = []
sprotRecList = []
tairRecList = []
filteredList = []
sprotFilteredList = []
tairFilteredList = []

###sprot reference filtering
SprotRef = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_3_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklists/blacklist_descline_sprot.txt", "r")
blacklist_sprot = des_blacklist.readlines()

for token in blacklist_sprot:
	desList_sprot.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))


###Tair reference filtering
TairRef = "/home/samaneh/AHRD/data/reference/nrTair/non_red_tair10_batch_1_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklists/blacklist_descline_tair.txt", "r")
blacklist_tair = des_blacklist.readlines()

for token in blacklist_tair:
	desList_tair.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))


#sprot filtering
for record in SeqIO.parse(SprotRef, "fasta"):
	for token in desList_sprot:
		if token.lower() in record.description.lower():
			if record.id not in sprotRecList:
				sprotRecList.append(record.id) # save the sequence id which CONTAINS blacklist tokens


#tair filtering
for record in SeqIO.parse(TairRef, "fasta"):
	for token in desList_tair:
		if token.lower() in record.description.lower():
			if record.id not in tairRecList:
				tairRecList.append(record.id) # save the sequence id which CONTAINS blacklist tokens


#############################################################################################
#### generate two new reference sets for each set ####

sprotRefFiltered = open("/home/samaneh/AHRD/data/reference/sprot_batch_3_references_filtered.fasta","w")	
sprotRefincBlacklist = open("/home/samaneh/AHRD/data/reference/sprot_batch_3_references_incBlacklist.fasta","w") # CONTAINS blacklist tokens

tairRefFiltered = open("/home/samaneh/AHRD/data/reference/tair_1_reference_filtered.fasta","w")	
tairRefincBlacklist = open("/home/samaneh/AHRD/data/reference/tair_1_reference_incBlacklist.fasta","w") # CONTAINS blacklist tokens

for record in SeqIO.parse(SprotRef, "fasta"):
	if record.id in sprotRecList:		
		SeqIO.write(record, sprotRefincBlacklist, "fasta")
	else:	
 		SeqIO.write(record, sprotRefFiltered, "fasta")
 		if record.id not in sprotFilteredList:
 			sprotFilteredList.append(record.id)

for record in SeqIO.parse(TairRef, "fasta"):
	if record.id in tairRecList:		
		SeqIO.write(record, tairRefincBlacklist, "fasta")
	else:	
 		SeqIO.write(record, tairRefFiltered, "fasta")
 		if record.id not in sprotFilteredList:
 			tairFilteredList.append(record.id)

sprotRefFiltered.close()
sprotRefincBlacklist.close()
tairRefFiltered.close()
tairRefincBlacklist.close()


################################################################################
#### generate two new seperated databases for each to apply in blast search ####

sprotDB = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"	

sprotDBFiltered_removed = open("/home/samaneh/AHRD/data/db/uniprot_sprot_filtered_removed.fasta","w")	
sprotDBincBlacklist_removed = open("/home/samaneh/AHRD/data/db/uniprot_sprot_incBlacklist_removed.fasta","w")


tairDB = "/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated.fasta"

tairDBFiltered_removed = open("/home/samaneh/AHRD/data/db/uniprot_TAIR10_filtered_removed.fasta","w")	
tairDBincBlacklist_removed = open("/home/samaneh/AHRD/data/db/uniprot_TAIR10_incBlacklist_removed.fasta","w")



for record in SeqIO.parse(sprotDB, "fasta"):
	if record.id not in sprotRecList:		
		SeqIO.write(record, sprotDBincBlacklist_removed, "fasta")
	elif record.id not in sprotFilteredList:	
 		SeqIO.write(record, sprotDBFiltered_removed, "fasta")

for record in SeqIO.parse(tairDB, "fasta"):
	if record.id not in tairRecList:		
		SeqIO.write(record, tairDBincBlacklist_removed, "fasta")
	elif record.id not in sprotFilteredList:	
 		SeqIO.write(record, tairDBFiltered_removed, "fasta")


###done
