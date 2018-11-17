# Module:		get_sample_list.py
# Description:	generate sample list, sample size = 288 (144 match + 144 mismatch)
# Note:			a. 80 known matched samples in training dataset
#				b. 80 (68 match + 16 mismatch) unknown status samples in testing dataset
#				c. generate new 128 mismatched samples


import pandas as pd
import csv
import os

data_dir = "/home/amber/Documents/Final-project/Step1/"

csv_infile = data_dir + "sum_tab_2.csv"
txt_file = data_dir + "txt_sum.txt"
csv_outfile = data_dir + "a_sum_tab.csv"

df = pd.read_csv(csv_infile, sep=",")

# print(len(df))
# print(len(df['RNAseq']))

fp = open(txt_file, 'w')

fp.write("sample\tClinical\tRNAseq\tProteomics\n")
prefix_train = "Training_"
prefix_test = "Testing_"

# 80 known matched samples in training dataset
for i in range(80):
	fp.write(df['sample'][i])
	fp.write('\t')
	fp.write(prefix_train + str(df['Clinical'][i]))
	fp.write('\t')
	fp.write(prefix_train + str(df['RNAseq'][i]))
	fp.write('\t')
	fp.write(prefix_train + str(df['Proteomics'][i]))
	fp.write('\n')

print("Training list completed!")

# 80 unknown status samples in testing dataset
for i in range(81):
	if (i != 0):
		fp.write("Testing_%d\tTesting_%d\tTesting_%d\tTesting_%d\n" % (i, i, i, i))

print("Testing list completed!")

# generate 128 mismatched samples in training dataset
for i in range(128):
	fp.write("New_%d\t" % (i + 1))
	if (i <= 77):
		fp.write(prefix_train + str(df['Clinical'][i]))
		fp.write('\t')
		fp.write(prefix_train + str(df['RNAseq'][i+1]))
		fp.write('\t')
		fp.write(prefix_train + str(df['Proteomics'][i+2]))
		fp.write('\n')
	else:
		fp.write(prefix_train + str(df['Clinical'][i-78]))
		fp.write('\t')
		fp.write(prefix_train + str(df['RNAseq'][i-76]))
		fp.write('\t')
		fp.write(prefix_train + str(df['Proteomics'][i-77]))
		fp.write('\n')

fp.close()

print("Random mismatched list completed!")

with open(csv_outfile, 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, dialect='excel')
	with open(txt_file, 'rb') as filein:
		for line in filein:
			line_list = line.strip('\n').split('\t')
			spamwriter.writerow(line_list)

print("Sample list with 288 pro+rna completed!")

csvfile.close()
os.remove(txt_file)