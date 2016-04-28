#!/usr/bin/env python

import sys

if __name__ == '__main__':
    g_list = []
    h_list = []
    r_list = []
    s_list = []
    f = True

    for line in sys.stdin:
        if f:
            f = False
            continue
        house, first, last = line.split(' ')
        name = first + ' ' + last
        name = name.rstrip()
        if house == 'G':
            g_list.append(name)
        elif house == 'H':
            h_list.append(name)
        elif house == 'R':
            r_list.append(name)
        elif house == 'S':
            s_list.append(name)
        else:
            print "FAILED"
            sys.exit(1)

    if g_list:
        print "Gryffindor:"
        for name in sorted(g_list):
            print name
    if h_list:
        print "Hufflepuff:"
        for name in sorted(h_list):
            print name
    if r_list:
        print "Ravenclaw:"
        for name in sorted(r_list):
            print name
    if s_list:
        print "Slytherin:"
        for name in sorted(s_list):
            print name

