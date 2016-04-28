#!/usr/bin/env python

import sys

NONE = 0
I_STATE = 1
P_STATE = 2

if __name__ == '__main__':
    f = True
    for line in sys.stdin:
        if f:
            f = False
            continue
        count = 0
        line = line.rstrip()
        state = NONE
        success = False
        for c in line:
            if state == NONE:
                if c == 'I':
                    state = I_STATE
            elif state == I_STATE:
                if c == 'P':
                    state = P_STATE
                else:
                    count = count + 1
            elif state == P_STATE:
                if c == 'C':
                    success = True
                    break
                else:
                    count = count + 1
        if success:
            print count
        else:
            print "INVALID"




