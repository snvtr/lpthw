import os, sys, argparse

# lmp3thw ex9:
#
# partial implementation of cut command
# options implemented: -d -c -f

### __defs__ ###

def parse_cut_params(arg_str):
    """ fills an array with elements to extract later """
    Temp0 = [0] * 255
    Temp1 = arg_str.split(',')
    
    if len(Temp1) <= 1:
        Temp0[int(Temp1[0])] = 1
        return Temp0

    for temp1 in Temp1:
        if temp1.find('-') >= 0:
            Temp2 = temp1.split('-')
            if Temp2[1] == '':
                Temp2[1] = '254'
            for i in range(int(Temp2[0]), int(Temp2[1])+1):
                Temp0[i] = 1
        else:
            Temp0[int(temp1[0])] = 1
    return Temp0

def cut_chars(Chars, filename):
    """ build the resulting string from charaters set by -c parameter """
# exception block for file opening is missing

    cut_line = []

    with open(filename, 'r') as f:

        for line in f:

            cut_line[:] = []

            if len(line.rstrip()) > 254:
                line_len = 254
            else:
                line_len = len(line.rstrip())

            for char_idx in range(line_len):
                if Chars[char_idx+1] == 1:
                    cut_line.append(line[char_idx:char_idx+1])

            print(''.join(cut_line)) # result for each line

    return True

def cut_fields(Fields, delim, filename):
    """ build the resulting string from fields split with delim and field list from -f parameter """

    cut_line = []

    print('debug. delimeter is: %s.' % delim)

    with open(filename,'r') as f:

        for line in f:

            cut_line[:] = []

            Temp0 = line.split(delim)
            for idx in range(1,len(Fields)): # min(len(Fields), len(Temp0)) 
                if Fields[idx] == 1:
                    if len(Temp0) >= idx:
                        cut_line.append(Temp0[idx-1])

            print(''.join(cut_line)) # result for each line 

    return True

### __main__ ###

parser = argparse.ArgumentParser(description='lmt3thw-ex9: pycut.py')
parser.add_argument('-d', '--delimiter', help='delimeter', nargs='+', action='store')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', '--characters', help='characters to print out: like c1,c2 or c1-c3,c4- etc', nargs=1, action='store', default='-1')
group.add_argument('-f', '--fields', help='fields to print out: like f1,f3,f4- or f3-f5,f7 etc', nargs=1, action='store', default='-1')
parser.add_argument('filename', help='filename to cut', action='store')
args = parser.parse_args()

# fill the Characters/Fields with values:
print('debug:',vars(args))

if args.characters == '-1':
    Filter = parse_cut_params(args.fields[0])
    cut_fields(Filter, args.delimiter[0].replace("'",''), args.filename)
else:
    Filter = parse_cut_params(args.characters[0])
    cut_chars(Filter, args.filename)
