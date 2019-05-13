#!/usr/bin/python3

# kinda implements -l, -a, -R and start path:
# ls -l -a -R .
# ls -laR ..
# ls -R -l /var/log/
# and so on

# currently without wildcards but it would be interesting to implement it

import os, sys   

### __subs__ ###

def show_list():

    for root, dirs, files in os.walk(option_path):
        print('Current dir: %s' % root)
        for i in sorted(dirs):
            if i.find('.') == 0 and not option_all:
                continue
            if option_long:
                st = os.stat(root + '\\' + i)
                f_stat = ''.join([str(st.st_uid),'.',str(st.st_gid),' ',str(oct(st.st_mode & 0o777))[2:]]) 
            else:
                f_stat = ''
            print('Dir : %15s %s' % (f_stat, i))

        for i in sorted(files):
            if i.find('.') == 0 and not option_all:
                continue
            if option_long:
                st = os.stat(root + '\\' + i)
                f_stat = ''.join([str(st.st_uid),'.',str(st.st_gid),' ',str(oct(st.st_mode & 0o777))[2:]]) 
            else:
                f_stat = ''
            print('File: %15s %s' % (f_stat, i))

        if not option_subd:
            del dirs[:]
        
    return


### __main__ ###

args = sys.argv[1:]

option_long = False
option_all  = False
option_subd = False
option_path = ''

Options = set()

for i in args:
    if i[0] == '-':  # then it is an option
        for c in i[1:]:
            Options.add(c)
    else:
        if option_path == '':
# this works only when the path is not a wildcard parameter. 
# To accomodate use of wildcards this should be changed to something else
            if os.access(i, os.R_OK):
                option_path = i # only the first option works, the rest is ignored to avoid ambiguity
            else:
                print('The path %s is not accessible' % i)

        else:
            print('The option %s is ignored, too many patterns' % i)

if option_path == '':
    option_path = '.' 

for i in Options:

    if i not in ('l','a','R','h','H'):
        print('Unknown option: %s' % i)
        continue

    if i == 'h' or i == 'H':
        print('Usage:\n\t-l: show more information\n\t-a: show all files\n\t-R: recurse into subdirectories\n\t-h, -H: this help\n\tPATH: start path to list file')
        sys.exit(0)
    if i == 'l':
        option_long = True
    if i == 'a':
        option_all = True
    if i == 'R':
        option_subd = True

show_list()