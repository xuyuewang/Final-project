# Module:		pca.py
# Description:	Do PCA for total matrix (Pro and RNA together)

import csv
import pandas as pd
import numpy as np
import random
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data_dir = "/home/amber/Documents/Final-project/data/"

csv_infile = data_dir + "a_total_matrix.csv"
txt_outfile = data_dir + "a_pca_matrix.txt"

df = pd.read_csv(csv_infile, sep=",")

df.pop('sample')
df.pop('RNAseq')
df.pop('Proteomics')
x_data = df.values

print("Dimensions: %d" % (len(x_data[0])))	# 13768
print("Size: %d" % (len(x_data)))			# 304
print(x_data[0][0])
# print(len(data[0])) # 304
# print(len(data))    # 13768

# print(data[0][0],data[0][1])

# random.shuffle(data)

# print(data[0][0],data[0][1])
# standardize the data.
scaler = StandardScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)

# print(x_data.shape)

# # rndperm = np.random.permutation(x_data)
# random.shuffle(x_data)

# print(x_data)

pca = PCA(n_components=60)
pca_result = pca.fit_transform(x_data)

print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(len(pca_result))		#304
print(len(pca_result[0]))	#20
print(pca_result)
print(pca_result[303][19])

fp = open(txt_outfile, 'w')

for i in range(len(pca_result)):
	for j in range(len(pca_result[0])):
		fp.write(str(pca_result[i][j]))
		if (j != 59):
			fp.write("\t")
		else:
			fp.write("\n")

fp.close()