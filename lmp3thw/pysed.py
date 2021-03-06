#!C:/Python37/python3.exe

# implements s/// command from sed. Outputs into a file or onto a console.
# 'functionized'

import os, sys, argparse
import re

### __defs__ ###

def pysed(args):

    try:
        if args.filename != '-':
            text_f = open(args.filename,'r')
        else:
            text_f = sys.stdin
    except:
        print('cannot open file %s for reading' % args.filename)

    Cache = []

    commands = args.script.strip("'").split('/')
        
    for line in text_f:
        Cache.append(re.sub(commands[1], commands[2], line.rstrip()))
    text_f.close()

    try:
        if args.inplace and args.filename != '-':
            text_f = open(args.filename,'w')
    except:
        print('cannot open file %s for writing' % args.filename)
        
    for line in Cache:
        if args.inplace and args.filename != '-':
            print(line, file=text_f)
        else:
            print(line)
            
    if args.inplace:
        text_f.close()

    return True

### __main__ ###

parser = argparse.ArgumentParser(description='lmt3thw-ex10: pysed.py')
parser.add_argument('-i', '--inplace', help='inplace editing', action='store_true')
parser.add_argument("script", help='sed script to perform', action='store')
parser.add_argument("filename", help='filename to edit', action='store')
args = parser.parse_args()

#print(vars(args))

if __name__ == '__main__':
    pysed(args)