import pandas as pd
import numpy as np
import sys

diff_file = sys.argv[1]
tax_file = sys.argv[2]
outfile = sys.argv[3]

if not diff_file or not tax_file or not outfile:
  sys.exit("Need to specify an input and output")

with open(diff_file, 'r') as openfile:
  diffs = pd.read_csv(openfile, sep='\t')
  diffs.rename(columns= {"Unnamed: 0":"Feature ID"}, inplace=True)

with open(tax_file, 'r') as openfile:
  tax = pd.read_csv(openfile, sep='\t')

merged = diffs.merge(tax)

merged.to_csv(str(outfile), sep='\t')
