#!/usr/bin/env python3

import sys

tfs = set()
pro_genes = set()

with open(sys.argv[1], "r") as tfs_genes:
        for line in tfs_genes:
                line=line.strip()
                if line.startswith("Gene stable ID Transcript stable ID"):
                        continue
                                #line.replace("Gene stable ID Transcript stable ID","")

                else:
                        tfs.add(line)


with open(sys.argv[2], "r") as proliferation_genes:

        for line in proliferation_genes:
                line = line.strip()
                if line.startswith("Gene stable ID"):
                        continue

                else:
                        pro_genes.add(line)

print ("Transcription Factors of Cell Proliferation Genes:", tfs & pro_genes)

