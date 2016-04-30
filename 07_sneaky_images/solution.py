#!/usr/bin/env python

import sys

output = ''
cur = ''
for val in sys.stdin.readline().rstrip().split():
    if val[2] in ('0', '1'):
        cur += val[2]
        if len(cur) >= 8:
            output += chr(int(cur, 2))
            cur = ''
    else:
        cur = ''
print output
