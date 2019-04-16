#!/usr/bin/python3

# Implements some uniq features, default uniq feature and -c option

import os, sys
import argparse
import string, random

### __subs__ ###

def random_string(length=20):
    
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

### __main__ ###

parser = argparse.ArgumentParser(description='for training purposes')
parser.add_argument('-c', '--count', help='count the number of repeating lines', action='store_true')
parser.add_argument('-u', '--uniq', help='uniq default behaviour, displays unique lines', action='store_true') # does not do anything
parser.add_argument('FILE', help='File to process, "-" means stdin', action='store')
args = parser.parse_args()

try:
    if args.FILE != '-':
        uniq_f = open(args.FILE,'r')
    else:
        uniq_f = sys.stdin
except:
    print('Cannot open file %s. Exiting.' % args.FILE)

random_str = random_string()
print(vars(args), random_str)

prev = random_str
cnt  = 1

for line in uniq_f:
    line = line.rstrip()
    if line == prev:
        cnt += 1
    else:
        if args.count and prev != random_str:
            print('%d %s' % (cnt, prev))
        elif prev != random_str:
            print('%s' % prev)
        cnt = 1
        prev = line

if args.count:
    print('%d %s' % (cnt, prev))
else:
    print('%s' % prev)

uniq_f.close()