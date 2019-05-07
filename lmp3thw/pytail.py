#!/usr/bin/python3

# Implements some tail features - show last N lines, show live line feed 

import os, sys, time
import argparse

### __subs__ ###

def pytail(feed, lines, fn, line_nums):
    """ kinda main() """

    if feed:
        live_feed(fn)
    else:
        try:
            lines = int(lines)
        except:
            lines = 0
        last_lines(lines, fn, line_nums)


def live_feed(filename):
    """ prints live stream of lines """

    if not os.path.isfile(filename):
        return False

    f_size = os.stat(filename).st_size
    fd = open(filename,'rt')

    if f_size > 200:
        fd.seek(f_size-200)

    line = fd.readline()
    while line: 
        print(line.rstrip())
        line = fd.readline()

    fd.close()

    while True:
        time.sleep(0.5)
        f_size_new = os.stat(filename).st_size
        if f_size_new > f_size:
            with open(filename,'rt') as fd:
                fd.seek(f_size-1)
                line = fd.readline()
                while line:
                    print(line.rstrip())
                    line = fd.readline()
            f_size = f_size_new


def last_lines(n, filename, line_numbers):
    """ prints last n lines """

    line_cnt = 0
    Lines = []
    with open(filename,'r') as fd:
        for line_cnt, line in enumerate(fd):
            Lines.append(line)

    if n > line_cnt:
        n = line_cnt

    for i in range(line_cnt-n+1, line_cnt+1):
        if line_numbers:
            print(i,Lines[i], end='')
        else:
            print(Lines[i], end='')

    return True

### __main__ ###

parser = argparse.ArgumentParser(description='for training purposes')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-F', '--feed', help='Taillike live feed', action='store_true') # does not do anything
group.add_argument('-n', '--lines', help='Show a NUMBER of last lines', action='store', nargs=1)
parser.add_argument('-N', '--numbers', help='Show line numbers', action='store_true')
parser.add_argument('FILE', help='File to process, "-" means stdin', action='store')
args = parser.parse_args()

print('debug:',vars(args))

if args.lines is not None:
    lines = args.lines[0]
else:
    lines = 0

pytail(args.feed, lines, args.FILE, args.numbers)