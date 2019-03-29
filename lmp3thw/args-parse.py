#C:/Python37/python3.exe

import sys, argparse

# lmp3thway, ex4-1

# -h, --help - shows this help
# -x, --opt1 - flag option #1
# -y, --opt2 - flag option #2
# -z, --opt3 - flag option #3
# -f, --file <path to a file> - path option
# -l, --log <path to a file> - log option
# -m, --mask <mask> - wildcard option

### _defs__ ###

    
### __main__() ###

parser = argparse.ArgumentParser(description='for training purposes')
parser.add_argument('-x', '--optX', help='flag option #1', action='store_true')
parser.add_argument('-y', '--optY', help='flag option #2', action='store_true')
parser.add_argument('-z', '--optZ', help='flag option #3', action='store_true')
parser.add_argument('-f', '--file', help='path option', nargs=1)
parser.add_argument('-l', '--log', help='log option', nargs=1)
parser.add_argument('-m', '--mask', help='wildcard option', nargs=1)
args = parser.parse_args()

print(vars(args))