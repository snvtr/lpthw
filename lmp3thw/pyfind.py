#!C:/Python37/python3.exe

# lmp3thw - ex7. исполнение команды find
# понимает два типа файлов - f/d и маски файлов
# реализует только функцию -print

import os, sys
import argparse
import fnmatch

### __defs__ ###

def check_wildcard(filename, pattern):
    """ проверяет имя переданное в параметрах относительно pattern в args.name """

    if filename.find('\\'):
        path_elements = filename.split('\\')
    else:
        path_elements = [filename]
        
    if any (fnmatch.fnmatch(path_element, pattern) for path_element in path_elements):
        return True

    return False

### __main__() ###

parser = argparse.ArgumentParser(description='lmp3thw ex6: basic find')
parser.add_argument('start_dir', help='folder to start search, default is .', action='store', default='.')
parser.add_argument('-type', help='file type (d, f)', default='f')
parser.add_argument('-name', help='filename or wildcard expression to search', default='*')
parser.add_argument('-print', help='print matching filenames', action='store_true')
args = parser.parse_args()
print('debug:'+args.start_dir)
print('debug:'+args.type)
print('debug:'+args.name)  # pattern
print('debug:'+str(args.print))

tree = os.walk(args.start_dir)

if args.type == 'd' and args.print:
    for i in tree:
        if check_wildcard(i[0], args.name):
            print(i[0])
elif args.type == 'f' and args.print:
    for i in tree:
        for file in i[2]:
            if check_wildcard(file, args.name):
                print(i[0]+'\\'+file)
