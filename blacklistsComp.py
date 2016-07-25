'''
@auther: Sam

'''
import numpy as np
import re


###Read the balacklists
tokenFile = open("/home/samaneh/AHRD/data/blacklist_token.txt", "r")
desFile = open("/home/samaneh/AHRD/data/blacklist_descline.txt", "r")
tokenList = tokenFile.readlines()
desList = desFile.readlines()

###remove unwanted sumbols to make comparison easier
exist = list()
desBlacklist = list()
tokenBlacklist = list()

for token in desList:
	desBlacklist.append(token.lstrip("(?i)^").rstrip("\r\n "))

for token in tokenList:
	tokenBlacklist.append(token.lstrip("(?i)").rstrip("\r\n "))

###find tokens that are in descline blacklist but not in token blasklist
###create an intersection blasklist of token and desclin blacklists
combList = tokenBlacklist	

for token in desBlacklist:
	if token in tokenBlacklist:
		exist.append(token)
	else:
		combList.append(token)	
		

existFile = open("/home/samaneh/AHRD/outputs/onlyInDesTokens","w")
existFile.write(' '.join(("tokens in descline blacklist which are also included in token blacklist are:",str(exist))))
existFile.close()

combFile = open("/home/samaneh/AHRD/outputs/combinedTokenBlacklist","w")
combFile.write(' '.join(("combination list: ",str(combList))))
combFile.close()
