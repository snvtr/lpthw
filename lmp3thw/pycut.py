import os, sys, argparse

# lmp3thw ex9:
#
# имитация части функционала cut
# реализует -d -c -f 

### __defs__ ###

def parse_chars(arg_str):
    return char_pattern

def parse_fields(arg_str):
    return field_pattern

def cut_chars(char_pattern):
    pass
    
def cut_fields(field_pattern):
    pass

### __main__ ###

parser = argparse.ArgumentParser(description='lmt3thw-ex8: pygrep.py')
parser.add_argument('-d', '--delimiter', help='delimeter', nargs=1, action='store')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', '--characters', help='characters to print out: like c1,c2 or c1-c3,c4- etc', nargs=1, action='store', default='0')
group.add_argument('-f', '--fields', help='fields to print out: like f1,f3,f4- or f3-f5,f7 etc', nargs=1, action='store', default='0')
parser.add_argument('filename', help='filename to cut', action='store')
args = parser.parse_args()


