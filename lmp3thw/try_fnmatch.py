
import os, sys, fnmatch

def try_fnmatch(filename, pattern):

    if filename[-1] == '\\':
        ''.join(filename,'*')

    filename.lstrip('\\')