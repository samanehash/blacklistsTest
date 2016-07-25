'''
@auther: Samaneh

'''
from Bio import SeqIO


#sprotInFile = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
tremblInFile = "/home/samaneh/AHRD/data/db/uniprot_trembl.fasta"
os = "OS=Blumeria"
desList = []

#sprotOutFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot_BG_removed.fasta", "w")
#for record in SeqIO.parse(sprotInFile, "fasta"):
#	if os not in record.description:
#		SeqIO.write(record, sprotOutFile, "fasta")
#sprotOutFile.close()

tremblOutFile = open("/home/samaneh/AHRD/data/db/uniprot_trembl_BG_removed.fasta", "w")
for record in SeqIO.parse(tremblInFile, "fasta"):
	if os not in record.description:
		SeqIO.write(record, tremblOutFile, "fasta")
tremblOutFile.close()

