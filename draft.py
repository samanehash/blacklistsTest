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
		self.preNoSpace = False
		self.sufNoSpace = False
		self.suffListLength = 0


	def findMax(self,descList):

		maxOne = ""
		for s in descList:
			if len(s)>len(maxOne):
				maxOne = s
		return maxOne		

	def prefixCheck(self, ncp1):

		prePrefixOk = False
		suffSuffixOk = False
		PrefixOk = False
		prefixFlag = False
		newNcp1 = newNcp2 = []
		pf = sf = ""

		prefixStree = st.STree(input=ncp1)
		self.prefix_longest_common_string, prefixWii = prefixStree.lcs()
		self.prefix_longest_common_string = self.prefix_longest_common_string.encode("ascii","ignore").lower()


		if self.prefix_longest_common_string != " ":
			for j in range(len(ncp1)):
				if self.prefix_longest_common_string in ncp1[j]:
					for word in self.prefix_longest_common_string.split():
						if word in ncp1[j].split():
							prefixOk = True	
							plcsStartingIndx = ncp1[j].find(self.prefix_longest_common_string) 
							plcsEndingIndx = plcsStartingIndx + len(self.prefix_longest_common_string) 
							if plcsStartingIndx > 0:	#checks if there is prefix before lcs in prefix string 
								newNcp1.append(ncp1[j][plcsStartingIndx:plcsEndingIndx])
								prePrefixOk = True
							elif plcsEndingIndx < len(ncp1[j]):	#checks if there is suffix after lcs in suffix string
								newNcp2.append(ncp1[j][plcsEndingIndx:])
								suffSuffixOk = True	

			if prePrefixOk == True:
				pf = self.prefixCount(newNcp1, self.prefix_longest_common_string.lstrip(" ").rstrip(" "))
			if suffSuffixOk == True:
				sf = self.suffixCount(newNcp2, self.prefix_longest_common_string.lstrip(" ").rstrip(" "))

			#before = self.longest_common_string
			if self.preNoSpace == False:
				self.longest_common_string = pf + " " + self.prefix_longest_common_string.lstrip(" ").rstrip(" ") + " " + sf + " " + self.longest_common_string
			elif self.preNoSpace == True:
				#print self.longest_common_string, "--after:"
				self.longest_common_string = pf + " " + self.prefix_longest_common_string.lstrip(" ").rstrip(" ") + " " + sf + self.longest_common_string
				#print self.longest_common_string


			prefixFlag = True	

				
		return prefixFlag	


	def suffixCheck(self, ncp2):
		
		prePrefixOk = False
		suffSuffixOk = False
		suffixOk =False
		suffixFlag = False
		newNcp1 = newNcp2 = []
		pf = sf = ""

		suffixStree = st.STree(input=ncp2)
		self.suffix_longest_common_string, suffixWii = suffixStree.lcs()
		self.suffix_longest_common_string = self.suffix_longest_common_string.encode("ascii","ignore").lower()


		if self.suffix_longest_common_string != " ":
			for j in range(len(ncp2)):
				if self.suffix_longest_common_string in ncp2[j]:
					for word in self.suffix_longest_common_string.split():
						if word in ncp2[j].split():
							suffixOk = True	
							slcsStartingIndx = ncp2[j].find(self.suffix_longest_common_string)
							slcsEndingIndx = slcsStartingIndx + len(self.suffix_longest_common_string) 
							if slcsStartingIndx > 0:
								newNcp1.append(ncp2[j][0:slcsStartingIndx])			
								prePrefixOk = True
							if slcsEndingIndx < len(ncp2[j]):
								newNcp2.append(ncp2[j][slcsEndingIndx:])		
								suffSuffixOk = True	
			
			if prePrefixOk == True:
				pf = self.prefixCount(newNcp1, self.suffix_longest_common_string.lstrip(" ").rstrip(" "))
			if suffSuffixOk == True:
				sf = self.suffixCount(newNcp2, self.suffix_longest_common_string.lstrip(" ").rstrip(" "))

			#before = self.longest_common_string
			if self.sufNoSpace ==False:		
				self.longest_common_string = self.longest_common_string + " " + pf + self.suffix_longest_common_string.lstrip(" ").rstrip(" ") + sf
			elif self.sufNoSpace == True:
				#print self.longest_common_string, "--after:"
				self.longest_common_string = self.longest_common_string + pf + self.suffix_longest_common_string.lstrip(" ").rstrip(" ") + sf
				#print self.longest_common_string

			suffixFlag = True		


		return suffixFlag


	def prefixCount(self, ncp1, lcs):

		prefixKeyList = []
		prefixDict = {i:ncp1.count(i) for i in ncp1} #count repeated prefixes in the list
		
		prefixMax = max(prefixDict.values())
		nullNumber = self.suffListLength - len(ncp1)
		if nullNumber <= prefixMax:
			for key, value in prefixDict.iteritems():	
				if value == prefixMax:
					if key != " ":
						prefixKeyList.append(key)		
			if len(prefixKeyList) > 1:		
				pf = prefixKeyList[0]
				for k in range(1,len(prefixKeyList)):
					pf = pf + "/" + prefixKeyList[k]		
			elif len(prefixKeyList) == 1:
				pf = prefixKeyList[0]
			else:
				pf = ""	
		else:
			pf = ""		

		return pf	
		
	def suffixCount(self, ncp2, lcs):

		suffixKeyList = []
		suffixDict = {j:ncp2.count(j) for j in ncp2} #count repreated suffixes in the list

		suffixMax = max(suffixDict.values())
		nullNumber = self.suffListLength - len(ncp2)
		if nullNumber <= suffixMax:
			for key, value in suffixDict.iteritems():
				if value == suffixMax:
					pat = re.compile("\d")
					f = pat.match(key)
					if key != " " and f == False:
						suffixKeyList.append(key)
			if len(suffixKeyList) > 1:		
				sf = suffixKeyList[0]
				for k in range(1,len(suffixKeyList)):
					sf = sf + "/" + suffixKeyList[k]			
			elif len(suffixKeyList) == 1:
				sf = " " + suffixKeyList[0]
			else:
				sf = ""	
		else:
			sf = ""

		return sf

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


	def pairwiseCheck(self, inputList):
		
		removeFlag = False
		base = max(inputList)
		threshold = (0.8*len(base))
		for i in range(len(inputList)):
			if len(inputList[i]) < threshold:
				removeFlag = True


	def makeSuffixTree(self, names, descriptions, resFile):

		suffixDict = dict()
		resultDic = dict() #dictionary of sequence ids with corresponding selected (representative) descriptions
		#longestLength = (l(descriptions))
		if not self.pairwiseCheck(descriptions):
			stree = st.STree(input=descriptions)
			self.longest_common_string, wii = stree.lcs()
			suffList = self.extractDescriptions(wii)
			self.suffListLength = len(suffList)
		##@sam## return all descriptions of a cluster and its selected longest common part of descriptions whose length is at least as long as 5% of the longest description of the cluster
			ncpDict = dict()	#dictionary whose keys are all non-conservative part (i.e prefix or suffix)(=NCP) and the values are the number of appearance in descriptions 
			compDict = dict()
			keysList = []

			self.longest_common_string = self.longest_common_string.encode("ascii","ignore").lstrip(" ").rstrip(" ") ##@sam## convert unicode to string
			initialMinimalLength = len(self.findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
			finalMinimalLength = len(self.findMax(descriptions))*0.8
			if len(self.longest_common_string) >= initialMinimalLength and self.longest_common_string != "protein":  ##@sam## check if the selected description meets the minimal length and ignore clusters with too short common longest descriprion
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
						if su[cpStartingPoint] != " ":
							self.preNoSpace = True	
					if cpFinishingPoint < suFinishingPoint:
						ncp2.append(su[cpFinishingPoint:suFinishingPoint])	
						if su[cpFinishingPoint] != " ":

							self.preNoSpace = True

				######?????????????#############		
				#if "enom" in ncp1 or "3n-pip" in ncp1:
				#	print ncp1, ncp2	

				### check prefixes and suffixes for possible longest_common_string extention 
				if ncp1:
					if len(ncp1) > (self.suffListLength - len(ncp1)):
						pCheck = self.prefixCheck(ncp1)	#if prefixCheck returns True i.e. self.longest_common_string has been extended
						if pCheck == False:
							self.prefixCount(ncp1, self.longest_common_string)	#otherwise it tries to find words from prefixes to add to self.longest_common_string

				if ncp2:
					if len(ncp2) > (self.suffListLength - len(ncp2)):
						sCheck = self.suffixCheck(ncp2)	#if suffixCheck returns True i.e. self.longest_common_string has been extended	
						if sCheck == False:
							self.suffixCount(ncp2, self.longest_common_string)	#otherwise it tries to find words from suffixes to add to self.longest_common_string
				#if "3-phosphoshikimate" in self.longest_common_string:
				#	print ncp1, ncp2, "sCheck= ", sCheck		
				if self.longest_common_string > finalMinimalLength:
					pat = re.compile("\d")
					f = pat.match(self.longest_common_string[len(self.longest_common_string)-1])
					if f == True:
						print self.longest_common_string
						self.longest_common_string = " ".join(self.longest_common_string.split(" ")[:-1])
					self.longest_common_string = self.longest_common_string.replace("putative","").replace("(fragment)","").replace(" truncated","").replace("truncated","").replace("homolog","").replace("probable","")
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
	clustersFile = open("/home/samaneh/AHRD/clustering/testClusterFile.txt","r")
	resultFile = open("/home/samaneh/AHRD/clustering/testClusterDescriptions_draftVersion.txt","w")
	d.extractDesc(clustersFile,resultFile)

if __name__ == "__main__":
	handler()


