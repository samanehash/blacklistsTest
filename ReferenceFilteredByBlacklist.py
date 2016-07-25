'''
@auther: Samaneh

'''
from Bio import SeqIO


ref = "/home/samaneh/AHRD/data/reference/test/non_red_sprot_batch_3_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklist_descline.txt", "r")
blacklist = des_blacklist.readlines()

desList = []
for token in blacklist:
	desList.append(token.lstrip("(?i)^").rstrip("\r\n ").replace("\s", " ").replace("+", ""))
recList = []

for record in SeqIO.parse(ref, "fasta"):
	for token in desList:
		if token.lower() in record.description.lower():
			if record.id not in recList:
				recList.append(record.id) 									

refFiltered = open("/home/samaneh/AHRD/data/reference/test/non_red_sprot_batch_3_references_filtered.fasta","w")	
for record in SeqIO.parse(ref, "fasta"):
	if record.id not in recList:		
 		SeqIO.write(record, refFiltered, "fasta")
refFiltered.close()