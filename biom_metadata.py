# create metadata tsv for biom table
# Requires biom (can nuse conda qiime2 env)
# Takes 1 mandatory input: biom table
# Also takes 1 optional input: output name

from biom.util import biom_open
from biom import Table, load_table
import sys

try:
    in_biom = sys.argv[1]
except IndexError:
  print("Creates a tsv of the metadata for a biom table")
  print("Input 1 (mandatory): biom table")
  print("Input 2 (optional): name of metadata tsv output.")
  exit()

#Import the biom table
biom_table = load_table(sys.argv[1])

#Extract the metadata
metadata = biom_table.metadata_to_dataframe(axis='observation')
metadata.index.name = "Feature ID"

#Get name for output
try:
    name = sys.argv[2]
except IndexError:
    name = sys.argv[1].split(".")[0] + "_metadata.tsv"

print("output name:", name)

#Write the output
metadata.to_csv(name, sep = '\t')
