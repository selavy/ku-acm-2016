#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        break;
    n = n - 1

    mydict = dict()
    for i, line in enumerate(sys.stdin):
        key, value = line.rstrip().split()
        mydict[key] = value
        if i >= n:
            break

    for line in sys.stdin:
        words = line.split()
        for word in words:
            if word in mydict:
                print mydict[word],
            else:
                print word,
