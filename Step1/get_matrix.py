# Module:		get_matrix.py
# Description:	get matrix combined pro and rna data together

import pandas as pd 
import hashlib
import os 

data_dir = "/home/amber/Documents/Final-project/Step1/"

train_pro = data_dir + "a_total_pro.csv"
train_rna = data_dir + "a_total_rna.csv"
tab_file = data_dir + "a_sum_tab.csv"
outputfile = data_dir + "a_total_matrix.csv"

d_tab = pd.read_csv(tab_file, sep=",")
d_tra_pro = pd.read_csv(train_pro, sep=",")
d_tra_rna = pd.read_csv(train_rna, sep=',')

columns = ['sample', 'Proteomics', 'RNAseq']
tab_df = d_tab[columns]

column_headers = list(d_tra_pro.columns.values)
print("Proteomicas dimensions: %d" % (len(column_headers)-1))
columns = column_headers
train_pro_df = d_tra_pro[columns]



column_headers = list(d_tra_rna.columns.values)
print("RNA-seq dimensions: %d" % (len(column_headers)-1))
columns = column_headers
train_rna_df = d_tra_rna[columns]

# y_data = df.pop('label').values
# print(column_headers)

result1 = pd.merge(tab_df, train_pro_df, on='Proteomics', how="left")
# result1 = result1.drop(['Proteomics', 'RNAseq'], axis=1)
# print(len(list(result1.columns.values)))
result2 = pd.merge(tab_df, train_rna_df, on='RNAseq', how="left")
result2 = result2.drop(['Proteomics', 'RNAseq'], axis=1)
# print(len(list(result2.columns.values)))

# print(type(result1))
# print(type(result2))
result3 = pd.merge(result1, result2, on='sample', how="left")

result3.to_csv(outputfile, index=False)
print("Matrix combined with proteomics and RNA data completed!")
print("Total dimensions: %d" % (len(list(result3.columns.values))-3))