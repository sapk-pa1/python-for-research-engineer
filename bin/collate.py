"""
Counts the occurance of the every words in the text documents and outputs them into the csv format 
"""

import sys 
import csv 
import string
import argparse
from collections import Counter
import utilities as util



def update_counts(reader, word_counts):
    """Update word counts with data from another reader/file."""
    # Skip the header line
    next(reader, None)  # Skip the first line from the reader
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)

def main(args): 
    word_counts = Counter()
    for fname in args.infiles:
        with open(fname, 'r') as reader:
            update_counts(reader, word_counts)
    util.collections_to_csv(word_counts, num=args.num)
 


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="__doc__")
    parser.add_argument("infiles", type=str,
                        nargs='*',
                        help="Input File name")
    """
    The number of expected arguments (nargs) is set to ?. This means
    that if an argument is given it will be used, but if none is provided,
    a default of '-' will be used instead. argparse.FileType('r') understands '-' to mean “read from standard input”; this is another
    Unix convention that many programs follow
    """
    parser.add_argument("-n","--num", type=int, default=None,
                        help="Output n most frequent word")
    args = parser.parse_args()
    main(args) 