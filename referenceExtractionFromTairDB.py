'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter

tairRefFile = open("/home/samaneh/AHRD/data/reference/non_red_tair10_selected_reference.fasta", "w")
tairDBFile = open("/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_selectedRemoved.fasta", "w")
tairTempFile = open("/home/samaneh/AHRD/data/db/TAIR10_temp_shouldBeRemoved.fasta", "w")


pattern1 = "NCBI"
pattern2 = "unknown"

counter = 0
tairDB = "/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated.fasta"
for record in SeqIO.parse(tairDB, "fasta"):				# parse sprot database fasta file
	if pattern1 in record.description.split(" "):			# each token of each description of database	
		if pattern2 not in record.description.split(" "):
			SeqIO.write(record, tairRefFile, "fasta")
			counter = counter + 1
		else:
			SeqIO.write(record, tairTempFile, "fasta")

	else:
		SeqIO.write(record, tairDBFile, "fasta")			

tairTempFile.close()
 
for record in SeqIO.parse("/home/samaneh/AHRD/data/db/TAIR10_temp_shouldBeRemoved.fasta", "fasta"):	
	if counter < 1500:
		SeqIO.write(record, tairRefFile, "fasta")
		counter = counter + 1		
	else:
		SeqIO.write(record, tairDBFile, "fasta")

tairRefFile.close()
tairDBFile.close()
tairTempFile.close()