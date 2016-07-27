'''
@auther: Samaneh Jozashoori

'''
import re
import numpy as np
import pandas as pd
from Bio import SeqIO
from pandas import ExcelWriter
import matplotlib.pyplot as plt
#from sklearn.metrics import confusion_matrix
import decimal as dc


#seperate proteins in AHRD result with "unknown protein" from those with normal descriptions
#all_both = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_batch_3_incBlacklist.xlsx"))
all_both = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair_1_incBlacklist.xlsx"))

allColnames_both = all_both.ix[2]
all_both = all_both.rename(columns=allColnames_both).drop(all_both.index[:3])

rownames_both = pd.Series(range(1,(len(all_both)+1)))
all_both.index = rownames_both

#select multiple columns
all_both = all_both[["Protein-Accession","Human-Readable-Description"]]

ahrdUnknownProteins_both = all_both[all_both["Human-Readable-Description"]=="Unknown protein"] #select proteins with unknown descriptions
ahrdDesProteins_both = all_both[all_both["Human-Readable-Description"]!="Unknown protein"] #select proteins with descriptions

descSeperation_both = ExcelWriter("/home/samaneh/AHRD/outputs/descExtractedFromTair1IncBlacklist_both.xlsx")			
				
ahrdUnknownProteins_both.to_excel(descSeperation_both, "ahrdUnknownProteins")
ahrdDesProteins_both.to_excel(descSeperation_both, "ahrdNormalDescriptions")
#refUncharacterizedProteins.to_excel(descSeperation_both, "refUncharacterizedProteins")
#refDesProteins.to_excel(descSeperation_both, "refNormalDescriptions")

descSeperation_both.save()


