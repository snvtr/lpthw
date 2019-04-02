#C:/Python37/python3.exe

# заготовка под pygrep, lmt3thw-ex8

import os, sys
import argparse, re, fnmatch

# script, pattern, filenames = sys.argv

# план:
# - реализовать поиск по маске файлов
# - возможно еще: -n - номер строки, -Р имя файла
# - запустить цикл по файлам
# - в цикле сделать проверку на совпадение по glob-у для файлов
# - далее, если файл подходит под маску, проверять совпадение по re

### __defs__ ###

def check_wildcard(filename, pattern):
    """ проверяет имя переданное в параметрах относительно pattern в args.name """

    if fnmatch.fnmatch(filename, pattern):
        return True

    return False

def grep(file, pattern):

    matches = []

    print('debug: opening file %s to look for %r' % (file, pattern))

    try:
        fd = open(file, 'r')
    except:
        print('cannot open file %s for reading. skipped' % file)

    for line in fd:
        pass

    fd.close()

    return matches

### __main__()

parser = argparse.ArgumentParser(description='lmt3thw-ex8: pygrep.py')
parser.add_argument('-R', '--recursive', help='recursive search', action='store_true')
parser.add_argument('-n', '--line-number', help='print line numbers', action='store_true')
parser.add_argument('-H', '--filename', help='print filename for each match', action='store_true')
parser.add_argument('grep_pattern', help='GREP_PATTERN to find', action='store')
parser.add_argument('file_pattern', help='filename FILE_PATTERN', action='store')
args = parser.parse_args()

print('debug:', vars(args))

tree = os.walk('.', topdown=True)

for i in tree:
    print('debug:',i)
#    if not args.recursive:
#        i[1] = []
    for file in i[2]:
        if check_wildcard(file, args.file_pattern):
            # тут можно уже разворачивать поиск внутри файла
            matching_lines = grep(file, args.grep_pattern)
            for i in matching_lines:
                if args.filename:
                    print(': '.join([file, i]))
                else:
                    print(i)
