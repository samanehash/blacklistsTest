'''
@auther: Samaneh

WORKING VERSION

'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import xlsxwriter
import re
import multiprocessing
from multiprocessing.dummy import Pool
#from suffix_tree import SuffixTree
from suffix_tree import GeneralisedSuffixTree 

###################################################################

### updates the suffixes dictionary
def suffixUpdate(s, suffixDic):

	if s in suffixDic.keys():
		suffixDic[s] = suffixDic[s] + 1
	else:
		suffixDic.update({s:1})
		
	return suffixDic

def makeSuffixTree(descriptions):

	stree = GeneralisedSuffixTree(descriptions)
	###has a function for extracting all shared substrings of the set of strings or all shared substrings of a given minimal length
	longestLength = 0
	longestDes = ""
	suffixDic = dict()

	for shared in stree.sharedSubstrings(): 
		longest = len(max(stree.sequences))
		for seq, start, end in shared:

			common = (stree.sequences[seq][start:end]).lower() 
			l = len(common)
			suffix = (stree.sequences[seq][end:]).lower()

			if l > longestLength:
				longestLength = l
				longestDes = common
				longestSuf = suffix
				suffixDic = suffixUpdate(suffix, suffixDic)
		
			if l == longestLength: 
				suffixDic = suffixUpdate(suffix, suffixDic)

### ATENTION: in finding the most frequent suffix another strategy might be needed when there are suffix with equal frequencies 
	for k,v in suffixDic.items():
		if v == max(suffixDic.values()):
			longestDes = longestDes + k 
	longestDes = re.sub("\(fragment[s]*\)","", longestDes)	
	longestDes = re.sub("putative","", longestDes)
	if len(longestDes) > (longest/10):  ###to remove the cluster in which the descriptions differ a lot from each 
										###other and a representative one cannot be selected	
		print longestDes, "l=", len(longestDes) , "\n", longestLength 

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
				makeSuffixTree(descs)
			
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



	


