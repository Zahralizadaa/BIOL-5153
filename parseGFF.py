#! /user/bin/env python3

import csv
import argparse
# from Bio import seqI0

# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# creat an argument parser project
parser = argparse.ArgumentParser(description= 'this script will parse a GFF file and extract each feature from the genome')

# add positional arguments 
parser.add_argument('gff', help = 'name of the GFF file')
parser.add_argument('fasta', help = 'name of the FASTA file')

# parse the arguments 
args = parser.parse_args()
# print(args.gff)

'''
# read in GFF file 
gff_input = '/home/codebind/Desktop/Scripts/watermelon.gff'


# fasta filename
fasta-input = '/home/codebind/Desktop/Scripts/watermelon.fsa'
'''

# open and read in FASTA file (with open(gff_input, 'r') as gff_in:)
with open (args.gff, 'r') as gff_in:
     # create a csv reader object 
     reader = csv.reader(gff_in, delimiter= '\t')
     # loop over all the lines in our reader object of the parse file 
     for line in reader:
         print(line)
         start = line [3]
         end = line[4]
         strand = line[6]
         print(start)
