#
# File name: readTranscriptsFile.py
# Authors: Arnar Þór Björgvinsson, Unnur Ása Bjarnadóttir, Sóley Lúðvíksdóttir
# Submission: 30.11.2018
# Course: Töl504M
# Instructor: Páll Melsted
# 
# =============================================================================
"""A function that reads in data from a fasta-file and returns a list 
   with query strings. 
"""
# =============================================================================
# Imports
# =============================================================================

from Bio.SeqIO.FastaIO import SimpleFastaParser

def readQuery(file):
    query = []
    with open(file, 'r') as f:
        for title, seq in SimpleFastaParser(f):
            query.append(seq)
    return query

#print(readQuery("../data/transcripts.fasta"))
