"""
Counts the occurance of the every words in the text documents and outputs them into the csv format 
"""

import sys 
import csv 
import string
import argparse
from collections import Counter
import utilities as util



def count_words(reader): 
    """Reads the occurance of each words in the string """
    text = reader.read() 
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word for word in npunc if word]
    words_count = Counter(word_list)
    return words_count  

def main(args): 

    word_count = count_words(args.infile) 
    util.collections_to_csv(word_count, num=args.num)
 


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="__doc__")
    parser.add_argument("infile", type=argparse.FileType('r'),
                        nargs='?',default='-',
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