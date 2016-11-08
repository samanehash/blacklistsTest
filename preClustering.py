'''
@auther: Samaneh

'''
from Bio import SeqIO

def prepareNamesList(clusterNamesFile):  

	idList = []
	lines = clusterNamesFile.readlines()
	for line in lines:
		words = line.split()
		if len(words)==1:
			idList.append(words[0])
	return idList

def filtering(isolatedList):

	sprot = "/home/samaneh/AHRD/data/db/uniprot_sprot.fasta"
	reducedSprot = open("/home/samaneh/AHRD/data/db/uniprot_sprot_filteredForClustering.fasta", "w")
	removingList = []

	for record in SeqIO.parse(sprot, "fasta"):
		for name in isolatedList:
			if name in record.name:
				removingList.append(record.id)

	for record in SeqIO.parse(sprot,"fasta"):
		if record.id not in removingList:
			SeqIO.write(record, reducedSprot, "fasta" )

	reducedSprot.close()


def handler():
	clusterFile = open("/home/samaneh/AHRD/clustering/clusters.txt","r")
	isolatedList = prepareNamesList(clusterFile)
	filtering(isolatedList)


if __name__ == "__main__":
	handler()