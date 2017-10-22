#!/usr/bin/env python3 

import sys 

genes = set()
pro_genes = set()

#with open ("/Users/admin/PFB2017_problemsets/Python5ProblemSet/alpaca_all_genes.tsv", "r") as all_genes: 

with open(sys.argv[1], "r") as all_genes:

	for line in all_genes:
		line=line.strip()
		if line.startswith("Gene stable ID"):
			continue
				#line.replace("Gene stable ID","")
		
		else:
			genes.add(line)


with open(sys.argv[2], "r") as proliferation_genes:

	for line in proliferation_genes:
		line = line.strip()
		if line.startswith("Gene stable ID"):
			continue

		else:
			pro_genes.add(line)

print("GENES IN COMMON:", genes & pro_genes)

#print("ALL GENES NOT CELL PROLIFERATION:", genes-pro_genes)


#print(pro_genes)

#print("All GENES:", genes ("\n"), "PROLIFERATION GENES:", pro_genes ("\n"))




