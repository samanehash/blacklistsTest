'''
@auther: Samaneh

Extract selected 1034 sequences ids to use later for generating a new fasta file including sprot descriptions

'''

from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import csv
import os
import json

###########################################################################################

selectedSeqsFile = open("/home/samaneh/eggNOG/output/clstrd_ref_eggNOG_descs.fasta","r")
sprotFile = open("/home/samaneh/AHRD/data/db/uniprot_sprot.fasta", "r")
newReferenceFile = open("/home/samaneh/eggNOG/output/clstrd_ref_sprot_descs.fasta","w")
idsList = []

for record in SeqIO.parse(selectedSeqsFile,"fasta"):
	seqAC = record.id.split("|")[1]
	idsList.append(seqAC)

for seq in SeqIO.parse(sprotFile,"fasta"):
	if seq.id.split("|")[1] in idsList:
		SeqIO.write(seq, newReferenceFile, "fasta")


	










