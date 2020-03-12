import argparse
import numpy as np
import re

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--directory")
	args = parser.parse_args()
	"./save/0312309/dccn/p7/pc/sum/sum.txt"
	with open("./save/0312/liu/pc/data/sum.txt", "r") as f:
		aa = []
		oa = []
		kappa = []
		for line in f.readlines():
			wordlist = re.split(", |:| ",line.strip())
			# print(wordlist)
			oa.append((float)(wordlist[0]))
			aa.append((float)(wordlist[1]))
			kappa.append((float)(wordlist[2]))
		# print(aa)
		# print(oa)
		# print(kappa)
		# exit()
		oamid = (np.max(oa) + np.min(oa)) / 2
		oadiff = oamid - np.min(oa)
		aamid = (np.max(aa) + np.min(aa)) / 2
		aadiff = aamid - np.min(aa)
		kpmid = (np.max(kappa) + np.min(kappa)) / 2
		kpdiff = kpmid - np.min(kappa)
		# oamid *=100
		# oadiff *=100
		aamid *=100
		aadiff *=100
		kpmid *=100
		kpdiff *=100

		print("%.2f±%.2f & %.2f±%.2f & %.2f±%.2f\\\\" % (oamid, oadiff, aamid, aadiff, kpmid, kpdiff))
