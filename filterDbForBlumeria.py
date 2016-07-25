'''
@auther: Sam

'''
from Bio import SeqIO
import re

###Read Data
###???refFile = open("/home/samaneh/AHRD/myScript/non_red_sprot_batch_3_references.fasta", "rU") # read reference fasta file
#seqs = SeqIO.read(refFile, "fasta")

###return sequence ID
#for record in SeqIO.parse(refFile, "fasta"):
#	print(record.id) 
	
### save all sequences as a list
###???seqs_list = list(SeqIO.parse(refFile, "fasta"))
###???p = re.compile(".*(Blumeria graminis).*")
#for i in range(0,len(seqs_list)):
#	print p.match(seqs_list[i].description)

###???for i in range(0,len(seqs_list)):
	#print seqs_list[i].description
	###???mch = p.match(seqs_list[i].description)
	###???print mch
# seqs_list[4].description

### save all sequences as a dictionary
#seqs_dict = SeqIO.index("/home/samaneh/AHRD/myScript/non_red_sprot_batch_3_references.fasta","fasta")
#print seqs_dict["sp|P64516|YECN_ECOL6"].description

###write records to a file
#sequences = ...
#outputFile = open("/home/samaneh/AHRD/myScript/non_red_sprot_batch_3_output.fasta", "w")
#SeqIO.write(sequences, outputFile, "fasta")
#outputFile.close()

#refFile.close()


#####################################################################################
#####################################################################################
#p = re.compile("ab*")

inFile = "/home/samaneh/AHRD/myScript/uniprot_sprot.fasta"
os = "OS=Blumeria"
desList = []

outFile = open("/home/samaneh/AHRD/myScript/uniprot_sprot_removed.fasta", "w")

for record in SeqIO.parse(inFile, "fasta"):
	if os not in record.description:
		#seqString = ">" + record.description + "\n" + record.seq
		SeqIO.write(record, outFile, "fasta")
outFile.close()
#SeqIO.write(desList, "uniprot_sprot_removed", "fasta")


