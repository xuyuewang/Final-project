# Module:		pca.py
# Description:	Do PCA for pro matrix

import csv
import pandas as pd
import numpy as np
import random
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data_dir = "/home/amber/Documents/Final-project/data/"

csv_infile = data_dir + "a_pro_matrix.csv"
txt_outfile = data_dir + "a_pca_pro.txt"

df = pd.read_csv(csv_infile, sep=",")

df.pop('sample')
# sample_id = df.pop('RNAseq').values
sample_id = df.pop('Proteomics').values
x_data = df.values

print("Dimensions: %d" % (len(x_data[0]))) 
print("Size: %d" % (len(x_data)))    			
print("Check for the first one: %lf" % (x_data[0][0]))

# standardize the data.
scaler = StandardScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)


pca = PCA(n_components=80)
pca_result = pca.fit_transform(x_data)

print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(len(pca_result))		#304
print(len(pca_result[0]))	#20
print(pca_result)

fp = open(txt_outfile, 'w')

for i in range(len(pca_result)):
	for j in range(len(pca_result[0])):
		fp.write(str(pca_result[i][j]))
		if (j != 79):
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