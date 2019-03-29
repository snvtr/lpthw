#C:/Python37/python.exe

# lmp3thw, ex5

import os, sys

args = [i for i in sys.argv]

if args[1] == '-h' or args[1] == '--help':
    print('\nDumps the content of files onto the screen.\n\nUsage:\n\tpycat.py <filename1> .. <filenameN>')
    sys.exit(0)

for i in range(1,len(args)):
    try:
        with open(args[i],'r') as fd:
            content = fd.readlines()
            for line in content:
                print(line.rstrip())
    except:
        print('Cannot open file %s for reading. Ignored.' % args[i])
