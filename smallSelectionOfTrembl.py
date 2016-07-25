'''
@auther: Samaneh

'''
from Bio import SeqIO


ref = "../uniprot_trembl.fasta"
records = list(SeqIO.parse(ref, "fasta"))


tremblSelection = open("../uniprot_trembl_selection.fasta","w")	
for record in records[1000000:1100000]:
		SeqIO.write(record, tremblSelection, "fasta")
for record in records[2000000:2100000]:
	SeqIO.write(record, tremblSelection, "fasta")
for record in records[3000000:3100000]:
		SeqIO.write(record, tremblSelection, "fasta")
for record in records[4000000:4100000]:
		SeqIO.write(record, tremblSelection, "fasta")
for record in records[5000000:5100000]:
		SeqIO.write(record, tremblSelection, "fasta")
for record in records[6000000:6050740]:
		SeqIO.write(record, tremblSelection, "fasta")

tremblSelection.close()