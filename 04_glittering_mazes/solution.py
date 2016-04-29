#!/usr/bin/env python

import sys
import copy
from collections import namedtuple

if __name__ == '__main__':
    Move = namedtuple('Move', ['x', 'y', 'maze', 'gem'])
    def is_gem(val):
        return val in ('R', 'E')
    def helper(prev):
        loc = prev.maze[prev.y][prev.x]
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        return loc, loc if is_gem(loc) else prev.gem, maze
    def go_left(prev):
        loc, gem, maze = helper(prev)
        return Move(x=prev.x-1, y=prev.y, maze=maze, gem=gem)
    def go_right(prev):
        loc, gem, maze = helper(prev)
        return Move(x=prev.x+1, y=prev.y, maze=maze, gem=gem)
    def go_up(prev):
        loc, gem, maze = helper(prev)
        return Move(x=prev.x, y=prev.y+1, maze=maze, gem=gem)
    def go_down(prev):
        loc, gem, maze = helper(prev)
        return Move(x=prev.x, y=prev.y-1, maze=maze, gem=gem)
    def valid(val):
        return val != '#' and val != 'X'
    def can_go_left(s):
        x = s.x - 1
        y = s.y
        if x < 0: return False
        val = s.maze[y][x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_right(s):
        x = s.x + 1
        y = s.y
        if x >= max_x: return False
        val = s.maze[y][x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_up(s):
        x = s.x
        y = s.y + 1
        if y >= max_y: return False
        val = s.maze[y][x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_down(s):
        x = s.x
        y = s.y - 1
        if y < 0: return False
        val = s.maze[y][x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    for line in sys.stdin:
        max_y, max_x = line.rstrip().split()
        max_x = int(max_x)
        max_y = int(max_y)
        break
    for line in sys.stdin:
        start_y, start_x = line.rstrip().split() # X and Y position for starting coords are backwards
        start_x = int(start_x)
        start_y = int(start_y)
        break
    maze = []
    for y, line in enumerate(sys.stdin):
        maze.append(list(line.rstrip()))
        if 'G' in line:
            goal_x = line.find('G')
            goal_y = y
    maze[start_y][start_x] = 'X'
    q = [Move(x=start_x, y=start_y, maze=maze, gem='')]
    while q:
        move = q.pop(0)
        if move.x == goal_x and move.y == goal_y: # reached goal!
            move.maze[move.y][move.x] = 'X'
            for y in move.maze: print ''.join(y)
            sys.exit(0)
        if can_go_left(move): q.append(go_left(move))
        if can_go_right(move): q.append(go_right(move))
        if can_go_up(move): q.append(go_up(move))
        if can_go_down(move): q.append(go_down(move))
    print "NO SOLUTION"
