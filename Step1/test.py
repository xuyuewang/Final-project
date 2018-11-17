# check the result of Step 1

import csv
import pandas as pd

data_dir = "/home/amber/Documents/Final-project/data/"

csv_file = data_dir + "a_total_rna.csv"

df = pd.read_csv(csv_file, sep=",")

print(df)