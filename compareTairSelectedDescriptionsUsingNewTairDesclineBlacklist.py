'''
@auther: Samaneh Jozashoori

'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib.backends.backend_pdf import PdfPages
from pandas import ExcelWriter

############################################################################

sprotList = []
sprotColnames = []
sprotRownames = []
 	 	
files = [	pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_selectedReference_both_oldBlacklists.xlsx")),
			pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_tair10_selectedReference_both_newTokenBlacklistIncGNs.xlsx"))]

writer1 = ExcelWriter("/home/samaneh/AHRD/outputs/tairSelectedDescriptionsComparison.xlsx")
writer2 = ExcelWriter("/home/samaneh/AHRD/outputs/tairSelectedDifferentDescriptions.xlsx")


for i in range(0,2):
	sprotList.append(files[i])
	sprotColnames.append(sprotList[i].ix[2])
	sprotRownames.append(pd.Series(range(1,(len(sprotList[i])-2))))
	sprotList[i] = sprotList[i].rename(columns=sprotColnames[i]).drop(sprotList[i].index[:3])
	sprotList[i].index = sprotRownames[i]

rfDes = pd.Series(sprotList[0]["Reference-Description"])
oldDes = pd.Series(sprotList[0]["Human-Readable-Description"])
newDes = pd.Series(sprotList[1]["Human-Readable-Description"])
df1 = pd.DataFrame({"reference description":rfDes, "AHRD using old blacklist description":oldDes, "AHRD using new blacklist description":newDes})


def comparison(rfList,oldList, newList):
	counter = 0
	diffOld = []
	diffNew = []
	diffRef = []
	for i in range(0,(len(oldList)-1)):
		old = str(oldList.iloc[i]).lower()
		new = str(newList.iloc[i]).lower()
		rf = str(rfList.iloc[i]).lower()
		if old not in new:
			diffOld.append(old)
			diffNew.append(new)	
			diffRef.append(rf)
			if "unknown" in rf:
				counter = counter + 1	
	print counter			
	df2 = pd.DataFrame({"reference description":diffRef, "AHRD using old blacklist description":diffOld, "AHRD using new blacklist description":diffNew})
	return df2

			
df2 = comparison(rfDes,oldDes, newDes)

df1.to_excel(writer1, "all descriptions", index=False)
df2.to_excel(writer2, "different descriptions", index=False)





