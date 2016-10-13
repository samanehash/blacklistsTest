'''
@auther: Samaneh

SO FAR FINAL VERSION

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import multiprocessing
from multiprocessing.dummy import Pool
#from suffix_tree import SuffixTree
#from suffix_tree import GeneralisedSuffixTree 
import suffixtreeLibrary as st
#from django.utils.encoding import smart_str


##################################################################################
##################################################################################
##################################################################################

def findMax(descList):

	maxOne = ""
	for s in descList:
		if len(s)>len(maxOne):
			maxOne = s
	return maxOne		

### updates the suffixes dictionary
def suffixUpdate(s, suffixDic):

	if s in suffixDic.keys():
		suffixDic[s] = suffixDic[s] + 1
	else:
		suffixDic.update({s:1})
		
	return suffixDic

def makeSuffixTree(names, descriptions):

	charList = []
	suffixDict = dict()
	#longestLength = (l(descriptions))
	stree = st.STree(input=descriptions)
	longest_common_string, wii = stree.lcs()
	wiiStr = wii.encode("utf8","ignore")

	##@sa## extracting all descriptions which are return from lcs functions of suffixtreeLibrary
	UPPAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
	for i in range(0,len(UPPAs)):
		y = unichr(UPPAs[i])
		charList.append(y)

	suffList = [] ##@sam## a list of all descriptions
	suffList.append(wiiStr)

	for c in charList:
		convertedC = c.encode("utf8","ignore")
		for j in range(0,len(suffList)):
			if convertedC in suffList[j]:
				temp = suffList[j]
				del suffList[j]	
				for token in temp.split(convertedC): 	
					suffList.append(token)
	del suffList[len(suffList)-1]				
	


	##@sam## return all descriptions of a cluster and its selected longest common part of descriptions whose length is at least as long as 5% of the longest description of the cluster
	longest_common_string = longest_common_string.encode("ascii","ignore") ##@sam## convert unicode to string
	l = [str(s) for s in longest_common_string.lstrip(" ").rstrip(" ").split(" ")] ##@sam## convert string to list
	minimalLength = len(findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
	if len(l) >= minimalLength:  ##@sam## check if the selected description meets the minimal length and ignore clusters with too short common longest descriprion
		#print "longest common:", "\n", longest_common_string,"\n", "all descriptions:", suffList, "\n", "*******"
		for n in names:
			suffixDict.update({n:longest_common_string})

	print suffixDict




########################################

def extractDesc(clstrsFile):
	
	tempFlag = False ### temporary flag until the file contains \n as the ending line
	seqNames = []
	names = []
	descs = []
	lines = clstrsFile.readlines()

	for i in range(0,len(lines)):
		if lines[i][0] == "#":
			tempFlag = False
			seqNames = []
			names = []
			descs = []
		elif lines[i][0] == "\n":
			if tempFlag == True:
			#i = 0
				makeSuffixTree(names, descs)	

		else:
			tempFlag = True
			seqNames = lines[i].split("|")
			for i in range(0,2):
				seqNames[i] = seqNames[i].strip(" ").strip("\n")
			names.append(seqNames[0])
			descs.append(seqNames[1])

def handler():

	clustersFile = open("/home/samaneh/Desktop/testClusterFile.txt","r")
	extractDesc(clustersFile)

if __name__ == "__main__":
	handler()

















