'''
@auther: Sam

'''
import pandas as pd
import numpy as np
from pandas import ExcelWriter #io.excel.xlsx.writer

### Read files corresponding to data set 3
bothDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_both_filteredReference_3.xlsx"))
noneDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_noBlacklist_filteredReference_3.xlsx"))
tokenDf = pd.read_excel(pd.ExcelFile("/home/samaneh/AHRD/outputs/xlsx/test_evaluator_output_token_filteredReference_3.xlsx"))

### Extract the columns names as they are placed in 3rd row
bothColnames = bothDf.ix[2]
noneColnames = noneDf.ix[2]
tokenColnames = tokenDf.ix[2]

rownames = pd.Series(range(1,(len(bothDf)-1)))

bothDf = bothDf.rename(columns=bothColnames).drop(bothDf.index[:2]) #remove first two blancked rows and rename columns to real columns names
bothDf.index = rownames #rename rows to start from 1
noneDf = noneDf.rename(columns=noneColnames).drop(noneDf.index[:2]) #remove first two blancked rows and rename columns to real columns names
noneDf.index = rownames #rename rows to start from 1
tokenDf = tokenDf.rename(columns=tokenColnames).drop(tokenDf.index[:2]) #remove first two blancked rows and rename columns to real columns names
tokenDf.index = rownames #rename rows to start from 1


###Filter evaluation score column
bothScores = bothDf[[0,3,9]]
noneScores = noneDf[[0,3,9]]
tokenScores = tokenDf[[0,3,9]]
dfb = pd.DataFrame()
dfn = pd.DataFrame()
dfbcom = pd.DataFrame()
dfncom = pd.DataFrame()

for i in range(1,(len(bothScores)-1)):
	bscore = bothScores.iloc[i][2]
	tscore = tokenScores.iloc[i][2]
	#print bscore, tscore
	if float(bscore)>float(tscore):
		col1 = bothScores.iloc[i][1]
		col2 = tokenScores.iloc[i][1]
		df2 = pd.DataFrame({"both description(higher score)":[col1], "token description":[col2]})
		dfb = dfb.append(df2)

for j in range(1,(len(noneScores)-1)):
	nscore = noneScores.iloc[j][2]
	tscore = tokenScores.iloc[j][2]
	#print nscore, tscore
	if float(nscore)>float(tscore):
		col1 = noneScores.iloc[j][1]
		col2 = tokenScores.iloc[j][1]
		df3 = pd.DataFrame({"none description(higher score)":[col1], "token description":[col2]})
		dfn = dfn.append(df3)


writer = ExcelWriter("/home/samaneh/AHRD/outputs/betterPerformed_filteredReference3.xlsx")
dfb.to_excel(writer, "sheet1", index=False)
dfn.to_excel(writer, "sheet2", index=False)
writer.save()
