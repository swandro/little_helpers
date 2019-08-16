# Add taxonomy to biom table

Not sure if column name of gOTUs has to be the same for metadata and taxa file

```
biom add-metadata \
-i input.biom \
--observation-metadata-fp gOTU_taxonomy.tsv \
--sc-separated Taxon \
-o output.biom

biom convert --to-tsv \
-i input.biom \
--header-key Taxon \
-o output.tsv

```
