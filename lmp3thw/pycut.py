import os, sys, argparse

# lmp3thw ex9:
#
# имитация части функционала cut
# реализует -d -c -f

### __defs__ ###

def parse_characters(arg_str):
    Temp1 = arg_str.split(',')
    for temp1 in Temp1:
        Temp2 = temp1.split('-')
        if Temp2[1] == '':
            Temp2[1] = '254'
            for i in range(int(Temp2[0]), int(Temp2[1])+1):
                Characters[i] = 1

def parse_fields(arg_str):
    Temp1 = arg_str.split(',')
    for temp1 in Temp1:
        Temp2 = temp1.split('-')
        if Temp2[1] == '':
            Temp2[1] = '254'
            for i in range(int(Temp2[0]), int(Temp2[1])+1):
                Fields[i] = 1

def cut_chars(char_pattern):
    pass

def cut_fields(field_pattern):
    pass

### __main__ ###

parser = argparse.ArgumentParser(description='lmt3thw-ex8: pygrep.py')
parser.add_argument('-d', '--delimiter', help='delimeter', nargs='+', action='store')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', '--characters', help='characters to print out: like c1,c2 or c1-c3,c4- etc', nargs=1, action='store', default='-1')
group.add_argument('-f', '--fields', help='fields to print out: like f1,f3,f4- or f3-f5,f7 etc', nargs=1, action='store', default='-1')
parser.add_argument('filename', help='filename to cut', action='store')
args = parser.parse_args()

# fill the Characters/Fields with values:
print('debug:',vars(args))

# maximal number of characters and fields is 255:
Characters = [0] * 255
Fields = [0] * 255

if args.characters == -1:
    parse_fields(args.fields[0])
else:
    parse_characters(args.fields[0])
