import os, sys, argparse

# lmp3thw ex9:
#
# имитация части функционала cut
# реализует -d -c -f

### __defs__ ###

def parse_cut_params(arg_str):
    """ заполняет массив для полей которые будут вырезаться """
    Temp0 = [0] * 255
    Temp1 = arg_str.split(',')
#    print('debug. split by comma:', Temp1)
    for temp1 in Temp1:
        Temp2 = temp1.split('-')
#        print('debug. split by hyphen:', Temp2)
        if Temp2[1] == '':
            Temp2[1] = '254'
        for i in range(int(Temp2[0]), int(Temp2[1])+1):
            Temp0[i] = 1
    return Temp0

def cut_chars(Chars, filename):
    """ для каждой строки из файла собираем результирующую строку по маске из chars """
    try:
        with open(filename, 'r') as f:
            cut_line[:] = []
            for line in f:
                if len(line) > 254:
                    line_len = 254
                else:
                    line_len = len(line)
                for char_idx in range(line_len):
                    if Chars[char_idx+1] == 1:
                        cut_line.append(line[char_idx:char_idx+1])
                print('debug. joined cut string:', ''.join(cut_line), '\n')
    except:
        print('Cannot open the file %s' % filename)
        sys.exit(1)

    return True

def cut_fields(Fields, delim, filename):
    """ для каждой строки из файла собираем поля порезанные по delim и списку полученных полей из fields """
    try:
        with open(filename,'r') as f:
            for line in f:
                pass # проверяем каждый символ и собираем строку
    except:
        print('Cannot open the file %r' % filename)
        sys.exit(1)

    return True
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

if args.characters == -1:
    Filter = parse_cut_params(args.fields[0])
#    print('debug:', Filter)
    cut_fields(Filter, args.delimiter, args.filename)
else:
    Filter = parse_cut_params(args.characters[0])
#    print('debug:', Filter)
    cut_chars(Filter, args.filename)
