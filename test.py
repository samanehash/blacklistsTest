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
#from suffix_tree import GeneralisedSuffixTree 
import suffixtreeLibrary as st
#from django.utils.encoding import smart_str

##################################################################
######################## library #################################
##################################################################



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

def makeSuffixTree(descriptions):

	#stree = GeneralisedSuffixTree(descriptions)
	#print findMax(descriptions), "\n", "****************"
	charList = []
	symb = ""
	#longestLength = (l(descriptions))
	stree = st.STree(input=descriptions)
	longest_common_string, wii = stree.lcs()
	UPPAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
	#print UPPAs
	#w = w.encode("ascii","ignore")
	wiiStr = []
	wiiStr.append(wii.encode("utf8","ignore"))
	print type(wiiStr[0])
	for i in range(0,len(UPPAs)):
		y = unichr(UPPAs[i])
		charList.append(y)
	for w in wii:
		for c in charList:
			if c in w:
				for j in range(0,len(wiiStr)):
					temp = []
					#print type(wiiStr[j])
					temp.append(wiiStr[j].split(c.encode("utf8","ignore")))
				wiiStr = []
				wiiStr = temp
				
	#wordsList = re.split(symb,wiiStr)
				
	#for s in range(0,len(symb)):
		#print type(symb[s])
		#wii = wii.split(symb[s])

	#wii.split(s for s in symb)
	#tempList = w.split((i.lstrip("u") for i in UPPAs[0] or UPPAs[1] or UPPAs[2] ))
	#d = [[s.encode("ascii") for s in l] for l in w]
	#UPPAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
	#print UPPAs[0].encode("utf8","ignore")
	#print UPPAs[0]
	#print w.split(UPPAs[0])
	#######tempList = [smart_str(i) for i in w]
	longest_common_string = longest_common_string.encode("ascii","ignore") ##@sam## convert unicode to string
	l = [str(s) for s in longest_common_string.lstrip(" ").rstrip(" ").split(" ")] ##@sam## convert string to list
	minimalLength = len(findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
	if len(l) > minimalLength:  ##@sam## check if the selected description meets the minimal length
		print longest_common_string,"\n", "w:", wiiStr, "\n", "*******"

	###has a function for extracting all shared substrings of the set of strings or all shared substrings of a given minimal length
	#longestLength = 0
	longestDes = ""
	suffixDic = dict()

	#for strng in stree.lcs(): 
		#longest = len(max(stree.sequences))
		#for seq, start, end in shared:
	#	print strng	
	#		common = (stree.sequences[seq][start:end]).lower() 
	#		l = len(common)
	#		suffix = (stree.sequences[seq][end:]).lower()
#
#			if l > longestLength:
#				longestLength = l
#				longestDes = common
#				longestSuf = suffix
#				suffixDic = suffixUpdate(suffix, suffixDic)
		
#			if l == longestLength: 
#				suffixDic = suffixUpdate(suffix, suffixDic)

### ATENTION: in finding the most frequent suffix another strategy might be needed when there are suffix with equal frequencies 
#	for k,v in suffixDic.items():
#		if v == max(suffixDic.values()):
#			longestDes = longestDes + k 
#	longestDes = re.sub("\(fragment[s]*\)","", longestDes)	
#	longestDes = re.sub("putative","", longestDes)
#	if len(longestDes) > (longest/10):  ###to remove the cluster in which the descriptions differ a lot from each 
										###other and a representative one cannot be selected	
#		print longestDes, "l=", len(longestDes) , "\n", longestLength 

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

















