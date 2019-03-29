#C:/Python37/python3.exe

import sys

# learn more python the hard way, ex4-1

# -h, --help - shows this help
# -x, --opt1 - flag option #1
# -y, --opt2 - flag option #2
# -z, --opt3 - flag option #3
# -f, --file <path to a file> - path option
# -l, --log <path to a file> - log option
# -m, --mask <mask> - wildcard option

### _defs__ ###

def flag_opt(idx):
    """ simple flag option """
    print('This is a simple flag option %s' % arg[idx])
    arg[idx] = ''
    return idx

def path_opt(idx):
    """ path option, takes path and kinda checks if file exists """
    if idx < len(arg)-1 and arg[idx+1][0] != '-':
        if arg[idx] == '-f' or arg[idx] == '--file':
            print('This is the file option with path %s' % arg[idx+1])
        if arg[idx] == '-l' or arg[idx] == '--log':
            print('This is the log option with path %s' % arg[idx+1])
    else:
        print('The parameter %s is not correctly formed' % arg[idx])
        arg[idx] = ''
        return idx
    arg[idx] = ''
    arg[idx+1] = ''
    return idx+1
    
def mask_opt(idx):
    """ wildcard option, kinda parses wildcards here """
    if idx < len(arg) and arg[idx+1][0] != '-':
        print('This is a wildcard option with an expression %s' % arg[idx+1])
    else:
        arg[idx] = ''
        return idx
    arg[idx] = ''
    arg[idx+1] = ''
    return idx+1

### __main__() ###

arg = [i for i in sys.argv]

if '-h' in arg or '--help' in arg:
    print('Usage:\n\t-h, --help: shows this help')
    sys.exit(0)

i = 1 
while i < len(arg):
    if arg[i] == '-x' or arg[i] == '--opt1' or arg[i] == '-y' or arg[i] == '--opt2' or arg[i] == '-z' or arg[i] == '--opt3':
        i = flag_opt(i) + 1
    elif arg[i] == '-f' or arg[i] == '--file' or arg[i] == '-l' or arg[i] == '--log':
        i = path_opt(i) + 1
    else:
        print('Unknown option %s is skipped' % arg[i])
        arg[i] = ''
        i += 1
