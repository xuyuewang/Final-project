# Module:		delete_NA.py
# Description:	a. delete parameters included NA
#				b. transform .tsv file into .csv file
#				c. reshape rows and columns
# Note:			Add a name for the first colum in .tsc file first

import csv
import os
import pandas as pd

data_dir = "/home/amber/Documents/542/data/"

tsv_file = data_dir + "total_pro.tsv"
csv_file = data_dir + "total_pro.csv"
txt_file = data_dir + "total_pro.txt"
csv_file2 = data_dir + "a_total_pro.csv"
prefix = "pro-"

csv_table = pd.read_table(tsv_file, sep = '\t')
csv_table.to_csv(csv_file, index = False)

with open(csv_file,'rb') as csvfile:
	reader = csv.reader(csvfile)
	rows = [row for row in reader]

data = []
sum_row = 0

for i in range(len(rows)):
	if '' not in rows[i]:
		data.append(rows[i])
		sum_row = sum_row + 1

csvfile.close()

print(sum_row)
print(len(data))
print(len(data[0]))

print("Delete parameters with NAs completed.")

fp = open(txt_file, 'w')

for i in range(len(data[0])):
	for j in range(len(data)):
		if ((i == 0) & (j != 0)):
			fp.write(prefix + data[j][i])
		else:
			fp.write(data[j][i])
		if (j != (len(data)-1)):
			fp.write('\t')
	fp.write("\n")

fp.close()

with open(csv_file2, 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, dialect='excel')
	with open(txt_file, 'rb') as filein:
		for line in filein:
			line_list = line.strip('\n').split('\t')
			spamwriter.writerow(line_list)

csvfile.close()

print("Format conversion completed.")
os.remove(txt_file)
os.remove(csv_file)