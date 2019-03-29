#!C:/Python37/python.exe

import os, sys
import argparse

### __defs__ ###

def check_vs_wildcard(filename):
    """ проверяет имя переданное в параметрах относительно pattern в args.name """
    pass


### __main__() ###

parser = argparse.ArgumentParser(description='lmp3thw ex6: basic find')
parser.add_argument('<root>', help='folder to start search, default is .', action='store', default='.')
parser.add_argument('-type', help='file type (d, f, l)', nargs=1, default='f')
parser.add_argument('-name', help='filename or wildcard expression to search', nargs=1, default='*')
parser.add_argument('-print', help='print matching filenames', action='store_true')
args = parser.parse_args()
print('debug:', vars(args))


