'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np

print pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_3.xlsx"))

allDesColnames = allDesDf.ix[2]

allDesDf = allDesDf.rename(columns=allDesColnames).drop(allDesDf.index[:3])

rownames = pd.Series(range(1,1493))
allDesDf.index = rownames

allDesDf = allDesDf["Human-Readable-Description"]





