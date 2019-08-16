
#!/bin/bash

if [ -e "$1" ]
  then
    qiime tools export --input-path "$1" --output-path temp
    mv temp/feature-table.biom "${1%.qza}".biom
    rm -r temp/
  else
    echo "Extracts qiime2 feature tables as biom files"
    echo "Usage: qza_to_biom file.qza"
    echo "Output: file.biom"
  fi
