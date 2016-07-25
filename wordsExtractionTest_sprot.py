'''
@auther: Samaneh

'''
from Bio import SeqIO
import re
import json

#db = "../data/reference/non_red_sprot_batch_3_references.fasta"
#db = "../uniprot_trembl_selection.fasta"
db = "../data/db/uniprot_sprot.fasta"
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
	word = pureDes.split(" ")[0]#.lower()
	word_2 = word.lower()
	#d. omit only numbers containing words from descriptions
	if not re.match(pattern, word_2) :
		if word_2 not in firstWordList:
			firstWordList.append(word_2)				

	#all words c. extract all words and the number of each apperance and put it in a dictionary
	words = (pureDes.split(" "))
	for w in words:
		w_2 = w.lower()
		#d. omit only numbers containing words from descriptions
		if not re.match(pattern, w_2):
			if w_2 not in wordsDictCount.keys():
				wordsDictCount.update({w_2:1})
			else:
				wordsDictCount[w_2] = wordsDictCount[w_2]+1				
	
#count the number of appearance of first words of descriptions in whole descriptions
#for wrd in firstWordList:
#	if wrd not in firstWordDictCount.keys():
#		count = wordsDictCount[wrd]
#		firstWordDictCount.update({wrd:count})


print "sprot_words_count", len(wordsDictCount.keys())


#for i in range(0,lSprot):
#	if sorted_wordsDictCount[i][0]=="protein":
#			print sorted_wordsDictCount[i]



#f = open('../outputs/firstWordsDictionary_sprot.json','w')
#sorted_firstWords_sprot = [(k,v) for v,k in sorted( [ (v,k) for k,v in firstWordDictCount.items() ] ) ]
#print sorted_firstWords_sprot
#json.dump(sorted_firstWords_sprot,f)
#f.close()



#f = open('../outputs/wordsDictionary_sprot.json','w')
#sorted_wordsDictCount = [(k,v) for v,k in sorted( [ (v,k) for k,v in wordsDictCount.items() ] ) ]
#print sorted_wordsDictCount
#json.dump(sorted_wordsDictCount,f)
#f.close()





