#!/bin/env python3
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

"""OTU clustering"""

import argparse
import sys
import os
import gzip
import statistics
import textwrap
from collections import Counter
# https://github.com/briney/nwalign3
# ftp://ftp.ncbi.nih.gov/blast/matrices/
import nwalign3 as nw

__author__ = "Maha GRAA"
__copyright__ = "Universite Paris Diderot"
__credits__ = ["Maha GRAA"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Maha GRAA"
__email__ = "mahagraa.geniebio@gmail.com"
__status__ = "Developpement"


def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def get_arguments():
    """Retrieves the arguments of the program.
      Returns: An object that contains the arguments
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description=__doc__, usage=
                                     "{0} -h"
                                     .format(sys.argv[0]))
    parser.add_argument('-i', '-amplicon_file', dest='amplicon_file', type=isfile, required=True, 
                        help="Amplicon is a compressed fasta file (.fasta.gz)")
    parser.add_argument('-s', '-minseqlen', dest='minseqlen', type=int, default = 400,
                        help="Minimum sequence length for dereplication (default 400)")
    parser.add_argument('-m', '-mincount', dest='mincount', type=int, default = 10,
                        help="Minimum count for dereplication  (default 10)")
    parser.add_argument('-c', '-chunk_size', dest='chunk_size', type=int, default = 100,
                        help="Chunk size for dereplication  (default 100)")
    parser.add_argument('-k', '-kmer_size', dest='kmer_size', type=int, default = 8,
                        help="kmer size for dereplication  (default 10)")
    parser.add_argument('-o', '-output_file', dest='output_file', type=str,
                        default="OTU.fasta", help="Output file")
    return parser.parse_args()

def read_fasta(amplicon_file, minseqlen):
    #min_seq = []
    seq =""
   
    #with gzip.open(amplicon_file, "rt") as  monfich:
        #for line in monfich:
            #if line.startswith('>') :
               # if seq ==
                #if len(seq)>= minseqlen:
                    #yield seq
                #seq = ""
            #elif line.startswith ('>') :
               # if seq == "":
                    #continue
            #else:
               # seq += line.strip()
        #if len(seq)>= minseqlen:
            #yield seq

    with gzip.open(amplicon_file, "rt") as  monfich:
        seq = ""
        for line in monfich:
            if line[0] == '>' :
             if seq == "" : 
                continue
             elif seq != "" :
                if len(seq)>= minseqlen:
                    yield seq
                seq =""
            else :
              seq += line.strip()
        if len(seq)>= minseqlen:
            yield seq


def dereplication_fulllength(amplicon_file, minseqlen, mincount):
    unique_sequences=[]
    occurences=[]

    sequences=read_fasta(amplicon_file, minseqlen)
    for sequence in sequences:

        if sequence not in unique_sequences:

            unique_sequences.append(sequence)
            occurences.append(1)
        else :
            index=unique_sequences.index(sequence)
            occurences[index]=occurences[index]+1

    oc_unique=sorted(zip(occurences,unique_sequences),reverse=True)
    unique_sorted=[seq for _,seq in oc_unique]
    occurences_sorted=[occ for occ,_ in oc_unique]
    print(occurences_sorted)
    for i in range(len(occurences_sorted)):
        if occurences_sorted[i]>mincount:
            yield [unique_sorted[i], occurences_sorted[i]]

def get_identity(alignment_list):
    """Prend en une liste de séquences alignées au format ["SE-QUENCE1", "SE-QUENCE2"]
    Retourne le pourcentage d'identite entre les deux."""
    pass

def abundance_greedy_clustering(amplicon_file, minseqlen, mincount, chunk_size, kmer_size):
    pass

def write_OTU(OTU_list, output_file):
    pass

#==============================================================
# Main program
#==============================================================
def main():
    """
    Main program function
    """
    # Get arguments
    args = get_arguments()
    # Votre programme ici

#==============================================================
# Chimera removal section
#==============================================================

def get_unique(ids):
    return {}.fromkeys(ids).keys()

def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))

def get_chunks(sequence, chunk_size):
    """Split sequences in a least 4 chunks
    """
    pass

def cut_kmer(sequence, kmer_size):
    """Cut sequence into kmers"""
    pass

def get_unique_kmer(kmer_dict, sequence, id_seq, kmer_size):
    pass

def detect_chimera(perc_identity_matrix):
    pass

def search_mates(kmer_dict, sequence, kmer_size):
    pass

def chimera_removal(amplicon_file, minseqlen, mincount, chunk_size, kmer_size):
    pass


if __name__ == '__main__':
    main()
