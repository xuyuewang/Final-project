# Module:		pca.py
# Description:	Do PCA for pro matrix

import csv
import pandas as pd
import numpy as np
from numpy import *
import random
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def loadDataSet(fileName):
    dataSet = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataSet.append(fltLine)
    return dataSet

data_dir = "/home/amber/Documents/Final-project/data/"

txt_infile1 = data_dir + "a_pca_pro.txt"
txt_infile2 = data_dir + "a_pca_rna.txt"
txt_outfile1 = data_dir + "a_pca_matrix_v2.txt"
txt_outfile2 = data_dir + "a_pca_matrix_v3.txt"

dataMat1 = mat(loadDataSet(txt_infile1))
dataMat2 = mat(loadDataSet(txt_infile2))


print "Proteomics data:", dataMat1.shape
print "RNA data:", dataMat2.shape

x_data = np.hstack((dataMat1,dataMat2))

print "RNA+Proteomics data:", x_data.shape
   			
# print("Check for the first one: %lf" % (x_data[0][0]))

pca = PCA(n_components=100)
pca_result = pca.fit_transform(x_data)

print "pca proportion\n", pca.explained_variance_ratio_
print "pca sum proportion:",sum(pca.explained_variance_ratio_)
print "pca result size:", pca_result.shape

# standardize the data.
scaler = StandardScaler()
scaler.fit(pca_result)
pca_result = scaler.transform(pca_result)

scaler = StandardScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)

# result after doing PCA with Pro + RNA
fp = open(txt_outfile1, 'w')

for i in range(len(pca_result)):
	for j in range(len(pca_result[0])):
		fp.write(str(pca_result[i][j]))
		if (j != 99):
			fp.write("\t")
		else:
			fp.write("\n")

fp.close()

# result only combine Pro + RNA
fp = open(txt_outfile2, 'w')

for i in range(len(x_data)):
	for j in range(len(x_data[0])):
		fp.write(str(x_data[i][j]))
		if (j != 159):
			fp.write("\t")
		else:
			fp.write("\n")

fp.close()

# with open(csv_file2, 'wb') as csvfile:
# 	spamwriter = csv.writer(csvfile, dialect='excel')
# 	with open(txt_file, 'rb') as filein:
# 		for line in filein:
# 			line_list = line.strip('\n').split('\t')
# 			spamwriter.writerow(line_list)

# csvfile.close()