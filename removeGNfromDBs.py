'''
@auther: Samaneh

'''
from Bio import SeqIO
import pandas as pd
import numpy as np

sprotDB = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
ahrdResult = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))


##colnames= = ["AHRD Score","Tair Score","SwissProt Score","Trembl Score"]

####extract the columns names as they are placed in 3rd row
dfColnames = ahrdResult.ix[2]
rownames = pd.Series(range(1,len(ahrdResult)-2))
ahrdResult = ahrdResult.rename(columns=dfColnames).drop(ahrdResult.index[:3])
ahrdResult.index = rownames
ahrdResult = ahrdResult["Human-Readable-Description"] #filter columns except evaluation scores
##ahrdResult.columns = colnames
#ahrdResult = ahrdResult.astype(float)



#tairFiltered = open("/home/samaneh/AHRD/data/db/TAIR10_pep_20101214_updated_batch_2_removed.fasta", "w")
for dbSeq in SeqIO.parse(sprotDB, "fasta"):
	#flag = False
	for refDB in ahrdResult:
		if dbSeq.id == refDB :
			print dbSeq
			#flag = True
	#if flag == False:			
	#	print 

#tairFiltered.close()