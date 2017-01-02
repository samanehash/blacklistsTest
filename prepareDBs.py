'''
@auther: Samaneh

Preparing the database for BLAST search by creatig a new fasta file 
out of the uniprot version of database excluding those sequences 
which are included in reference file

'''
from Bio import SeqIO


sprotInFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta","r")
referenceFile = open("/home/samaneh/eggNOG/output/clstrd_ref_myAlgo_descs.fasta","r")
excludingIds = []

for seq in SeqIO.parse(referenceFile,"fasta") :
	excludingIds.append(seq.id.split("|")[1])

sprotOutFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot_clstrd_myAlgo_removed.fasta", "w")
for record in SeqIO.parse(sprotInFile, "fasta"):
	recordId = record.id.split("|")[1]
	if recordId not in excludingIds:
		SeqIO.write(record, sprotOutFile, "fasta")
sprotOutFile.close()


