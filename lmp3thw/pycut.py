import os, sys, argparse

# lmp3thw ex9:
#
# имитация части функционала cut
# реализует -d -c -f 

### __defs__ ###



### __main__ ###

parser = argparse.ArgumentParser(description='lmt3thw-ex8: pygrep.py')
parser.add_argument('-d', '--delimiter', help='delimeter', nargs=1, action='store')
parser.add_argument('-c', '--characters', help='characters to print out: like x1,x2 or x1-x3,x4- etc', nargs=1, action='store', default='0')
parser.add_argument('-f', '--fields', help='fields to print out: like f1,f3,f4- or f3-f5,f7 etc', nargs=1, action='store', default='0')
parser.add_argument('filename', help='filename to cut', action='store')
args = parser.parse_args()

if args.characters != '0' and args.fields != '0':
    print('It is impossible to use -c and -f parameters together.')
    sys.exit(1)

