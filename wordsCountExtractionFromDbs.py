'''
@auther: Samaneh

'''
from Bio import SeqIO
import re
import json

db = "../data/reference/non_red_sprot_batch_3_references.fasta"
#db = "../uniprot_trembl_selection.fasta"
#db = "../uniprot_sprot.fasta"
seqs = SeqIO.parse(db, "fasta")

firstWordList = []
testList = []

wordsDictCount = dict()
firstWordDictCount = dict()
pattern = "^[0-9]*\.*-*[0-9]*$"

for seq in seqs:

	#a.omit name from description
	des = str(seq.description).strip(str(seq.name)).strip(" ")
	#b.omit unusable end part of the description
	pureDes = re.sub("OS=.*","",des)
	#first word c. extract the first word and put it in a list
	word = pureDes.split(" ")[0]
	#d. omit only numbers containing words from descriptions
	if not re.match(pattern, word) :
		if word not in firstWordList:
			firstWordList.append(word)	

	#all words c. extract all words and the number of each apperance and put it in a dictionary
	words = pureDes.split(" ")
	for w in words:
		#d. omit only numbers containing words from descriptions
		if not re.match(pattern, w):
			if w.lower() not in wordsDictCount.keys():
				wordsDictCount.update({w:1})
			else:
				wordsDictCount[w] = wordsDictCount[w]+1
	
#count the number of appearance of first words of descriptions in whole descriptions
for wrd in firstWordList:
	if wrd not in firstWordDictCount.keys():
		count = wordsDictCount[wrd]
		firstWordDictCount.update({wrd:count})


sortedSprot = [(k,v) for v,k in sorted( [ (v,k) for k,v in data_sprot.items() ] ) ]
lSprot = len(sortedSprot)
print "Sprot: " , sortedSprot[lSprot-10:lSprot]

sortedTrembl = [(k,v) for v,k in sorted( [ (v,k) for k,v in data_trembl.items() ] ) ]
lTrembl = len(sortedTrembl)
print "Trembl" , sortedTrembl[lTrembl-10:lTrembl]




#################f = open('../json/firstWords_sprot.json','w')
#################sorted_firstWords_sprot = [(k,v) for v,k in sorted( [ (v,k) for k,v in firstWords_sprot.items() ] ) ]
#print 10 most appearing words
#l = len(sorted_firstWords_sprot)
#print "Sprot: " , sorted_firstWords_sprot[l-10:l]
###############json.dump(sorted_firstWords_sprot,f)
################f.close()


##############f = open('../json/wordsDictionary_sprot.json','w')
###############sorted_wordsDictCount = [(k,v) for v,k in sorted( [ (v,k) for k,v in wordsDictCount.items() ] ) ]
#print 10 most appearing words
#l = len(sorted_wordsDictCount)
#print "Sprot: " , sorted_wordsDictCount[l-10:l]
##########json.dump(sorted_wordsDictCount,f)
############f.close()


#############f = open('../json/firstWordCount_sprot.json','w')
############sorted_firstWordDictCount = [(k,v) for v,k in sorted( [ (v,k) for k,v in firstWordDictCount.items() ] ) ]
#print 10 most appearing words
#l = len(sorted_firstWordDictCount)
#print "Sprot: " , sorted_firstWordDictCount[l-10:l]
##############json.dump(sorted_firstWordDictCount,f)
############f.close()



###############################################################################################################
################################################statistics#####################################################

#mean calculation
#mean_sprot = int(np.ceil(np.mean(data_sprot.values())))
#mean_trembl = int(np.ceil(np.mean(data_trembl.values())))

#t-test
#p = stats.ttest_1sample(tempList_sprot,mean_sprot)

#standard deviation calculation
#std_sprot = np.std(data_sprot.values())
#std_trembl = np.std(data_trembl.values())







