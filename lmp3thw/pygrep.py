#C:/Python37/python3.exe

# lmt3thw-ex8, implementation of grep command

import os, sys
import argparse, re, fnmatch

# script, pattern, filenames = sys.argv

# план:
# - searches a string against a wildcard filename pattern
# - options implemented: -n - string number, -Р - filename that contains a matched string

### __defs__ ###

def check_wildcard(filename, pattern):
    """ проверяет имя переданное в параметрах относительно pattern в args.name """

    if fnmatch.fnmatch(filename, pattern):
        return True

    return False

def grep(file, pattern):

    global compiled_pattern
    matches = []

#    print('debug: opening file %s to look for %r' % (file, pattern))

    try:
        fd = open(file, 'r')
    except:
        print('cannot open file %s for reading. skipped' % file)
        return

    line_count = 1
    for line in fd:
        output = ''
        if compiled_pattern.search(line) is not None:
            #print('debug: filename: %r line count: %r matched line: %r' % (file, line_count, line))
            if args.filename:
                output = file + ': '
            if args.line_number:
                output += str(line_count) + ': '
            output += line
            print(output.rstrip())
            line_count += 1

    fd.close()
    return

### __main__()

parser = argparse.ArgumentParser(description='lmt3thw-ex8: pygrep.py')
parser.add_argument('-R', '--recursive', help='recursive search', action='store_true')
parser.add_argument('-n', '--line-number', help='print line numbers', action='store_true')
parser.add_argument('-H', '--filename', help='print filename for each match', action='store_true')
parser.add_argument('grep_pattern', help='GREP_PATTERN to find', action='store')
parser.add_argument('file_pattern', help='filename FILE_PATTERN', action='store')
args = parser.parse_args()

#print('debug:', vars(args))

compiled_pattern = re.compile(args.grep_pattern)
tree = os.walk('.', topdown=True)

for i in tree:
    #print('debug:',i)
    if not args.recursive:
        i[1][:] = [] # clearing this value means that os.walk does not dive into subfolders. Documented performance
    for file in i[2]:
        if check_wildcard(file, args.file_pattern):
            # Here we search for a string in a file:
            rc = grep(i[0]+'\\'+file, args.grep_pattern)
