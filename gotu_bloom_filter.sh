#!/bin/bash

if [ -e "$1" ]
  then
    grep -v -f /Users/swandro/Documents/Databases/bloom_filter/bloom_gOTUs.txt "$1"
  else
    echo "Biom table in tsv format must be given."
    echo "Rows must contin gOTU ID.s"
  fi
