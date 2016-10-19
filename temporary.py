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
import json
#from django.utils.encoding import smart_str

##################################################################################
##################################################################################
##################################################################################

class clusters():

	def __init__(self):

		self.suffixDic = dict()
		self.longest_common_string = ""
		self.prefix_longest_common_string = ""
		self. suffix_longest_common_string = ""


	def findMax(self,descList):

		maxOne = ""
		for s in descList:
			if len(s)>len(maxOne):
				maxOne = s
		return maxOne		

	def prefixCheck(self, ncp1):

		PrefixOk = False

		prefixFlag = False
		prefixStree = st.STree(input=ncp1)
		self.prefix_longest_common_string, prefixWii = prefixStree.lcs()
		self.prefix_longest_common_string = self.prefix_longest_common_string.encode("ascii","ignore").lstrip(" ").rstrip(" ").lower()
		#if "p3n-pipo" in self.prefix_longest_common_string or "genome" in self.prefix_longest_common_string:
			#print self.prefix_longest_common_string
		for i in range(len(ncp1)):
			if ncp1[i] == self.prefix_longest_common_string:
				PrefixOk = True	
		if PrefixOk == True:
			before = self.longest_common_string
			self.longest_common_string = self.prefix_longest_common_string + " " + self.longest_common_string
			#print self.prefix_longest_common_string, " + ", before, "--- extended: ", self.longest_common_string
			prefixFlag = True
		#print "prefix:", self.prefix_longest_common_string, "--- lcs: ", self.longest_common_string
		
			
		return prefixFlag	

	def suffixCheck(self, ncp2):
		
		suffixOk =False

		suffixFlag = False
		suffixStree = st.STree(input=ncp2)
		self.suffix_longest_common_string, suffixWii = suffixStree.lcs()
		self.suffix_longest_common_string = self.suffix_longest_common_string.encode("ascii","ignore").lstrip(" ").rstrip(" ").lower()
		for j in range(len(ncp2)):
			if ncp2[j] == self.suffix_longest_common_string:
				suffixOk = True
		if suffixOk == True:
			before = self.longest_common_string		
			self.longest_common_string = self.longest_common_string + " " + self.suffix_longest_common_string
			#print self.suffix_longest_common_string, " + ", before, "--- extended: ", self.longest_common_string
			suffixFlag = True

		return suffixFlag


	def prefixCount(self, ncp1):

		prefixKeyList = []
		prefixDict = {i:ncp1.count(i) for i in ncp1} #count repeated prefixes in the list
		
		prefixMax = max(prefixDict.values())

		for key, value in prefixDict.iteritems():	
			if value == prefixMax:
				prefixKeyList.append(key)		
		if len(prefixKeyList) > 1:
			#print prefixKeyList		
			st = prefixKeyList[0]
			for k in range(1,len(prefixKeyList)):
				st = st + "/" + prefixKeyList[k]
				#print "---> ", st 	
			self.longest_common_string = st + self.longest_common_string	
		else:
			self.longest_common_string = prefixKeyList[0] + self.longest_common_string	

		
	def suffixCount(self, ncp2):

		suffixKeyList = []
		suffixDict = {j:ncp2.count(j) for j in ncp2} #count repreated suffixes in the list

		suffixMax = max(suffixDict.values())

		for key, value in suffixDict.iteritems():
			if value == suffixMax:
				suffixKeyList.append(key)
		if len(suffixKeyList) > 1:		
			st = suffixKeyList[0]
			for k in range(1,len(suffixKeyList)):
				st = st + "/" + suffixKeyList[k]	
			self.longest_common_string = self.longest_common_string	+ " " + st		
		else:
			self.longest_common_string = " " + suffixKeyList[0] + self.longest_common_string	


	def extractDescriptions(self,wii):

		suffList = []
		charList = []
		wiiStr = wii.encode("utf8","ignore")		
		##@sa## extracting all descriptions which are return from lcs functions of suffixtreeLibrary
		UPPAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
		for i in range(len(UPPAs)):
			y = unichr(UPPAs[i])
			charList.append(y)

		##@sam## a list of all descriptions
		suffList.append(wiiStr)

		##@sam## generating a list of all descriptions
		for c in charList:
			convertedC = c.encode("utf8","ignore")
			for j in range(len(suffList)):
				if convertedC in suffList[j]:
					temp = suffList[j]
					del suffList[j]	
					for token in temp.split(convertedC): 	
						token = token.replace("putative","").replace("(fragment)","").replace("(fragments)","").replace(" truncated","").replace("truncated","").replace("homolog","").replace("probable","")
						token = token.lstrip().rstrip()
						suffList.append(token)
		del suffList[len(suffList)-1]
		return suffList



	def makeSuffixTree(self, names, descriptions, resFile):

		suffixDict = dict()
		resultDic = dict() #dictionary of sequence ids with corresponding selected (representative) descriptions
		#longestLength = (l(descriptions))
		stree = st.STree(input=descriptions)
		self.longest_common_string, wii = stree.lcs()
		suffList = self.extractDescriptions(wii)

	##@sam## return all descriptions of a cluster and its selected longest common part of descriptions whose length is at least as long as 5% of the longest description of the cluster
		ncpDict = dict()	#dictionary whose keys are all non-conservative part (i.e prefix or suffix)(=NCP) and the values are the number of appearance in descriptions 
		compDict = dict()
		keysList = []

		self.longest_common_string = self.longest_common_string.encode("ascii","ignore").lstrip(" ").rstrip(" ") ##@sam## convert unicode to string
		minimalLength = len(self.findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
		if len(self.longest_common_string) >= minimalLength and self.longest_common_string != "protein":  ##@sam## check if the selected description meets the minimal length and ignore clusters with too short common longest descriprion
			ncp1 = [] # list of prefixes of longest_common_string of all descriptions
			ncp2 = [] # list of suffixes of longest_common_string of all descriptions
			wholeDes = ""
			allTheSame = False
			for su in suffList:
				cpStartingPoint = su.find(self.longest_common_string)	#finds the starting index of longest_common_string
				lcsLen = len(self.longest_common_string)	
				cpFinishingPoint = cpStartingPoint + lcsLen #finds the ending index of longest_commom_string
 				suFinishingPoint = len(su)
				if cpStartingPoint > 0:
					s = su[0:cpStartingPoint]
					ncp1.append(s)
					#if "p3n-pipo" in s or "genome" in s:
					#	print s
				if cpFinishingPoint < suFinishingPoint:
					ncp2.append(su[cpFinishingPoint:suFinishingPoint])
			######?????????????#############		
			#if "enom" in ncp1 or "3n-pip" in ncp1:
			#	print ncp1, ncp2	

			### check prefixes and suffixes for possible longest_common_string extention 
			if ncp1:
				pCheck = self.prefixCheck(ncp1)	#if prefixCheck returns True i.e. self.longest_common_string has been extended
				if pCheck == False:
					self.prefixCount(ncp1)	#otherwise it tries to find words from prefixes to add to self.longest_common_string
			if ncp2:
				sCheck = self.suffixCheck(ncp2)	#if suffixCheck returns True i.e. self.longest_common_string has been extended	
				if sCheck == False:
					self.suffixCount(ncp2)	#otherwise it tries to find words from suffixes to add to self.longest_common_string


			self.longest_common_string = self.longest_common_string.replace("putative","").replace("(fragment)","").replace(" truncated","").replace("homolog","").replace("probable","")
			resFile.write("longest common:" + "\n" + self.longest_common_string + "\n" + "all descriptions:" + str(suffList) + "\n" + "*******" + "\n")


			for n in names:
				resultDic.update({n:self.longest_common_string})
			##@sam## write the dictionary into a json file:
			#outFile = open("/home/samaneh/AHRD/clustering/seqIDsAndDescriptions","w")
			#json.dump(resultDic, outFile)	
		return resultDic



########################################
	# @staticmethod ##@sam## create static method:
	def extractDesc(self,clstrsFile,resFile):
		
		tempFlag = False ### temporary flag until the file contains \n as the ending line
		seqNames = []
		names = []
		descs = []
		lines = clstrsFile.readlines()

		for i in range(len(lines)):
			if lines[i][0] == "#":
				tempFlag = False
				seqNames = []
				names = []
				descs = []
			elif lines[i][0] == "\n":
				if tempFlag == True:
				#i = 0
					resultDictionary = self.makeSuffixTree(names, descs, resFile)	

			else:
				tempFlag = True
				seqNames = lines[i].split("|")
				for i in range(0,2):
					seqNames[i] = seqNames[i].strip(" ").strip("\n")
				seqNames[1] = seqNames[1].replace("putative","").replace("(fragment)","").replace("(fragments)","").replace(" truncated","").replace("truncated","").replace("homolog","").replace("probable","")
				seqNames[1] = seqNames[1].lstrip().rstrip()
				names.append(seqNames[0])
				descs.append(seqNames[1])

		####from here you can start generateing new fata file using resultdictionary:


def handler():

	d = clusters()
	clustersFile = open("/home/samaneh/AHRD/clustering/clusteredDescriptions_final.txt","r")
	resultFile = open("/home/samaneh/AHRD/clustering/testTemporary.txt","w")
	d.extractDesc(clustersFile,resultFile)

if __name__ == "__main__":
	handler()


