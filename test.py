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

##################################################################################
##################################################################################
##################################################################################

class clusters():

	def __init__(self):

		self.suffixDic = dict()
		self.longest_common_string = ""



	def findMax(self,descList):

		maxOne = ""
		for s in descList:
			if len(s)>len(maxOne):
				maxOne = s
		return maxOne		


	def makeSuffixTree(self, names, descriptions):


		charList = []
		suffixDict = dict()
		suffixDic = dict()
		#longestLength = (l(descriptions))
		stree = st.STree(input=descriptions)
		self.longest_common_string, wii = stree.lcs()
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
		self.longest_common_string = self.longest_common_string.encode("ascii","ignore") ##@sam## convert unicode to string
		l = [str(s) for s in self.longest_common_string.lstrip(" ").rstrip(" ").split(" ")] ##@sam## convert string to list
		minimalLength = len(self.findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
		if len(l) >= minimalLength:  ##@sam## check if the selected description meets the minimal length and ignore clusters with too short common longest descriprion
			#print "longest common:", "\n", longest_common_string,"\n", "all descriptions:", suffList, "\n", "*******"
			for n in names:
				self.suffixDic.update({n:self.longest_common_string})

		#for des in suffList:


		print "longest common:", "\n", self.longest_common_string,"\n", "all descriptions:", self.suffixDic, "\n", "*******" 



##@sam## manual longest common string extraction
	###has a function for extracting all shared substrings of the set of strings or all shared substrings of a given minimal length
	#longestLength = 0
	#longestDes = ""
	#suffixDic = dict()

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
	# @staticmethod ##@sam## create satatic method:
	def extractDesc(self,clstrsFile):
		
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
					self.makeSuffixTree(names, descs)	

			else:
				tempFlag = True
				seqNames = lines[i].split("|")
				for i in range(0,2):
					seqNames[i] = seqNames[i].strip(" ").strip("\n")
				names.append(seqNames[0])
				descs.append(seqNames[1])

def handler():

	d = clusters()
	clustersFile = open("/home/samaneh/Desktop/testClusterFile.txt","r")
	d.extractDesc(clustersFile)

if __name__ == "__main__":
	handler()








