#!/usr/bin/python3

# a little exercise on wildcard matching

import os, sys, fnmatch

script, start_dir, pattern = sys.argv

### __defs__ ###

def try_fnmatch(filename, pattern):

    if filename[-1] == '\\':
        ''.join(filename,'*')

    filename.lstrip('\\')
    
def check_wildcard(full_filename, pattern):
    """ checks a filename against the pattern в args.name """

    if fnmatch.fnmatch(full_filename, pattern):
        return True

    return False
    
### __main__() ###
    
tree = os.walk(start_dir)

for i in tree:
    print(i[0])
    for j in i[2]:
        if check_wildcard('\\'.join([i[0],j]), pattern):
            print('%s matches the pattern %s' % ('\\'.join([i[0],j]), pattern))
