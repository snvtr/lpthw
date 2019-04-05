#!C:/Python37/python3.exe

import os, sys, argparse
import re

### __main__() ###

parser = argparse.ArgumentParser(description='lmt3thw-ex10: pysed.py')
parser.add_argument('-i', '--inplace', help='inplace editing', action='store_true')
parser.add_argument("script", help='sed script to perform', action='store')
parser.add_argument("filename", help='filename to edit', action='store')
args = parser.parse_args()

print(vars(args))

try:
    text_f = open(args.filename,'r')
except:
    print('cannot open file %s for reading' % args.filename)

Cache = []

commands = args.script.strip("'").split('/')
    
for line in text_f:
    Cache.append(re.sub(commands[1], commands[2], line.rstrip()))
text_f.close()

if args.inplace:
    try:
        text_f = open(args.filename,'w')
    except:
        print('cannot open file %s for writing' % args.filename)
    
for line in Cache:
    if args.inplace:
        print(line, file=text_f)
    else:
        print(line)
        
if args.inplace:
    text_f.close()