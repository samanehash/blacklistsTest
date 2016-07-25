'''
@auther: Samaneh

'''
from Bio import SeqIO


SprotRef = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_3_references.fasta"
TairRef = "/home/samaneh/AHRD/data/reference/nrTair/non_red_tair10_batch_1_references.fasta"
BlumeriaRef = "/home/samaneh/AHRD/data/reference/blumeria_graminis_references.fasta"


des_blacklist = open("/home/samaneh/AHRD/data/blacklist_descline.txt", "r")
blacklist = des_blacklist.readlines()

desList = []
sprotRecList = []
tairRecList =[]
blumeriaRecList = []

for token in blacklist:
	desList.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))
recList = []

#sprot filtering
for record in SeqIO.parse(SprotRef, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				sprotRecList.append(record.id) 									

#tair filtering
for record in SeqIO.parse(TairRef, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():			
			if record.id not in recList:
				tairRecList.append(record.id)

#blumeria filtering
for record in SeqIO.parse(BlumeriaRef, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				blumeriaRecList.append(record.id)



sprotRefFiltered = open("/home/samaneh/AHRD/data/reference/sprot_batch_3_references_filtered.fasta","w")	
tairRefFiltered = open("/home/samaneh/AHRD/data/reference/tair_1_reference_filtered.fasta","w")	
blumeriaRefFiltered = open("/home/samaneh/AHRD/data/reference/blumeria_references_filtered.fasta","w")	

for record in SeqIO.parse(SprotRef, "fasta"):
	if record.id not in sprotRecList:		
 		SeqIO.write(record, sprotRefFiltered, "fasta")
sprotRefFiltered.close()

for record in SeqIO.parse(TairRef, "fasta"):
	if record.id not in tairRecList:		
 		SeqIO.write(record, tairRefFiltered, "fasta")
tairRefFiltered.close()

for record in SeqIO.parse(BlumeriaRef, "fasta"):
	if record.id not in blumeriaRecList:		
 		SeqIO.write(record, blumeriaRefFiltered, "fasta")
blumeriaRefFiltered.close()