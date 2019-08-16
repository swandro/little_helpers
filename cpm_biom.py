#Convert biom table to cpm

from biom import Table, load_table
from biom.util import biom_open
import sys
import numpy as np
import pandas as pd



biom_file = sys.argv[1]
if not biom_file:
  print("Provide input biom table")
  exit

biom_table = load_table(biom_file)


#Function to multiply all nonzero values by 1000000
def cpm(a,b,c):
  return(a*1000000)

#Transform table
biom_table.transform(cpm)

#Write output
output_name = biom_file.split(".biom")[0] + "_cpm.biom"
with biom_open(output_name, 'w') as outfile:
  biom_table.to_hdf5(outfile, "cpm")
