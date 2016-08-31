'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
##########################################################################


row2 = 0
writer2 = xlsxwriter.Workbook("/home/samaneh/AHRD/outputs/tairNewTokenCheck_final.xlsx")
worksheet2 = writer2.add_worksheet()

l = []
pattern1 = "NCBI"
pattern2 = "unknown"
sprotDB = "/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated.fasta"
for dbSeq in SeqIO.parse(sprotDB, "fasta"):				# parse sprot database fasta file
	if pattern1 in dbSeq.description.split(" "):			# each token of each description of database	
			if pattern2 not in dbSeq.description.split(" "):
				worksheet2.write(row2,0,dbSeq.description) #.strip(dbSeq.name).strip("| Symbols: |"))
				row2 = row2 + 1



