'''
@auther: Samaneh

'''
from Bio import SeqIO
from pandas import ExcelWriter
import numpy as np
import pandas as pd

###sprot
SprotRef1 = "/home/samaneh/AHRD/data/reference/non_red_sprot_batch_3_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklists/blacklist_descline_sprot", "r")
blacklist = des_blacklist.readlines()


###Tair
TairRef1 = "/home/samaneh/AHRD/data/reference/nrTair/non_red_tair10_batch_1_references.fasta"
des_blacklist = open("/home/samaneh/AHRD/data/blacklists/blacklist_descline_tair", "r")
blacklist = des_blacklist.readlines()


