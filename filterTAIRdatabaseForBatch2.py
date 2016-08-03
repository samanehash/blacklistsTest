'''
@auther: Samaneh

'''
from Bio import SeqIO


tairDB = "/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated.fasta"
tair2Reference = "/home/samaneh/AHRD/data/reference/non_red_tair10_batch_2_references.fasta"


tairFiltered = open("/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated_batch_2_removed.fasta", "w")
for dbSeq in SeqIO.parse(tairDB, "fasta"):
	flag = False
	for refDB in SeqIO.parse(tair2Reference, "fasta"):
		if dbSeq.id == refDB.id :
			flag = True
	if flag == False:			
		SeqIO.write(dbSeq, tairFiltered, "fasta")

tairFiltered.close()

