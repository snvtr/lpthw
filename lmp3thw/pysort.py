#!/usr/bin/python3

#
# quick and dirty sort implementation. Does not check if the first element is a valid integer during numeric sort.
#

import os, sys
import argparse

### __subs__() ###

def numeric_compare(x):
    elements1 = x.split(' ')
    return int(elements1[0])

### __main__ () ###

parser = argparse.ArgumentParser(description='lmp3thw: ex10, pysort.py')
parser.add_argument('-r', '--reverse', help='reverse sort', action='store_true')
parser.add_argument('-i', '--ignore-case', help='ignore case', action='store_true')
parser.add_argument('-g', '--numeric', help='numeric sort', action='store_true')
parser.add_argument('FILE', help='input file', action='store')
args = parser.parse_args()

print(vars(args))

if args.FILE == '-':
    input_f = sys.stdin
else:
    try:
        input_f = open(args.FILE,'r')
    except:
        print('Cannot open file %s for reading. Exiting' % args.FILE)
        sys.exit(-1)

Lines = []
for i in input_f:
    Lines.append(i.rstrip())

if args.ignore_case:
    Sorted = sorted(Lines, key=str.lower, reverse=args.reverse)
elif not args.numeric:
    Sorted = sorted(Lines, reverse=args.reverse)
elif args.numeric:
    Sorted = sorted(Lines, key=numeric_compare, reverse=args.reverse)

for i in Sorted:
    print(i)