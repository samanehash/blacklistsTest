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


	def makeSuffixTree(self, names, descriptions, resFile):


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
		suDict = dict()	#dictionary whose keys are all NCP and the values are the number of appearance in descriptions 
		originalDescDict = dict()
		keysList = []

		self.longest_common_string = self.longest_common_string.encode("ascii","ignore").lstrip(" ").rstrip(" ") ##@sam## convert unicode to string
		minimalLength = len(self.findMax(descriptions))/20 ##@sam## define the minimal lenth of accepted common description
		if len(self.longest_common_string) >= minimalLength and self.longest_common_string != "protein":  ##@sam## check if the selected description meets the minimal length and ignore clusters with too short common longest descriprion
			self.longest_common_string = self.longest_common_string.replace("putative","").replace("(fragment)","").replace(" truncated","")

			for su in suffList:
				suMod = su.replace("putative","").replace("(fragment)","").replace(" truncated","")	#removing non-informative part of the description
				pure = suMod.replace(self.longest_common_string,"").strip(" ")	#extract the non-conservative part (i.e prefix or suffix)(=NCP) of the description
				if pure in suDict.keys():	#NCP already exists in the dictionary
					suDict.update({pure:suDict[pure]+1})	#number of appearance of this NCP in the descriptions
				else:
					if pure != "":
						suDict.update({pure:1})	#add the NCP as a new item to the dictionary
						originalDescDict.update({pure:su})	
			keysList = []
			for di in suDict.keys(): 	
				v = max(suDict.values())	#find the NCP with the highest appearance (=maxNCP) 
				threshold = 0.6 * (len(suDict))	
				if v >= threshold:	#if maxNCP is at least 60% number of all NCPs:
					for key, value in suDict.iteritems():	
						if value==v:
							#print value, "---", suDict
							keysList.append(key)		
					if len(keysList) == 1:	#if there is only one highly appeared NCP:
						self.longest_common_string = originalDescDict[key]	#the lcs would be replaced by that NCP's complete decription 
					else:
						wordIndex = originalDescDict[key].find(keysList[0])	#the starting index of NCP
						wordLength = len(keysList[0])	
						startingPoint = wordIndex + wordLength + 1	
						string = originalDescDict[keysList[0]].rstrip(" ")
						for k in range(1,len(keysList)):
							string = string[:startingPoint] + "/" + keysList[k] + string[startingPoint:] 
						self.longest_common_string = string	

			self.longest_common_string = self.longest_common_string.replace("putative","").replace("(fragment)","").replace(" truncated","")
			resFile.write("longest common:" + "\n"+self.longest_common_string+"\n"+"all descriptions:"+str(suffList)+"\n"+"*******"+"\n")



			for n in names:
				self.suffixDic.update({n:self.longest_common_string})


########################################
	# @staticmethod ##@sam## create satatic method:
	def extractDesc(self,clstrsFile,resFile):
		
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
					self.makeSuffixTree(names, descs, resFile)	

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
	resultFile = open("/home/samaneh/AHRD/clustering/testClusterDescriptions_secondTest.txt","w")
	d.extractDesc(clustersFile,resultFile)

if __name__ == "__main__":
	handler()


