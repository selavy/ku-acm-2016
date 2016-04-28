#!/usr/bin/env python

import sys

for line in sys.stdin:
    max_x, max_y = line.rstrip().split()
    max_x = int(max_x)
    max_y = int(max_y)
    break;
for line in sys.stdin:
    x, y = line.rstrip().split()
    x = int(x)
    y = int(y)
    break;
print "Max X: ", max_x
print "Max Y: ", max_y
print "X: ", x
print "Y: ", y

maze = []
for line in sys.stdin:
    maze.append(line.rstrip())

print maze


