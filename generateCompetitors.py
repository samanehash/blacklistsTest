'''
@auther: Samaneh


'''

from Bio import SeqIO
import re

######################################################################

eggnog = open("/home/samaneh/eggNOG/output/clstrd_ref_eggNOG_descs.fasta", "r")
eggnogCom = open("/home/samaneh/eggNOG/output/clstrd_ref_eggNOG_descs.tsv", "w")

myAlgo = open("/home/samaneh/eggNOG/output/clstrd_ref_myAlgo_descs.fasta", "r")
myAlgoCom = open("/home/samaneh/eggNOG/output/clstrd_ref_myAlgo_descs.tsv", "w")

for record in SeqIO.parse(eggnog, "fasta"):
	ac = record.id.strip(" ")
	desc = record.description.strip(record.name).lstrip(" ")
	desc = re.sub("OS=.*", "", desc)
	eggnogCom.write(ac)
	eggnogCom.write("\t")
	eggnogCom.write(desc)
	eggnogCom.write("\n")

for record in SeqIO.parse(myAlgo, "fasta"):
	ac = record.id.strip(" ")
	desc = record.description.strip(record.name).lstrip(" ")
	desc = re.sub("OS=.*", "", desc)
	myAlgoCom.write(ac)
	myAlgoCom.write("\t")
	myAlgoCom.write(desc)
	myAlgoCom.write("\n")	


