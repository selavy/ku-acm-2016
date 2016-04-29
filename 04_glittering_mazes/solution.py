#!/usr/bin/env python

import sys
import copy
from collections import namedtuple

Move = namedtuple('Move', ['x', 'y', 'maze', 'gem', 'path'])

if __name__ == '__main__':
    def is_gem(val):
        return val == 'R' or val == 'E'
    def go_left(prev):
        loc = prev.maze[prev.y][prev.x]
        gem = loc if is_gem(loc) else prev.gem
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        path = copy.deepcopy(prev.path)
        path.append([prev.x-1, prev.y])
        return Move(x=prev.x-1, y=prev.y, maze=maze, gem=gem, path=path)
    def go_right(prev):
        loc = prev.maze[prev.y][prev.x]
        gem = loc if is_gem(loc) else prev.gem
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        path = copy.deepcopy(prev.path)
        path.append([prev.x+1, prev.y])
        return Move(x=prev.x+1, y=prev.y, maze=maze, gem=gem, path=path)
    def go_up(prev):
        loc = prev.maze[prev.y][prev.x]
        gem = loc if is_gem(loc) else prev.gem
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        path = copy.deepcopy(prev.path)
        path.append([prev.x, prev.y+1])
        return Move(x=prev.x, y=prev.y+1, maze=maze, gem=gem, path=path)
    def go_down(prev):
        loc = prev.maze[prev.y][prev.x]
        gem = loc if is_gem(loc) else prev.gem
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        path = copy.deepcopy(prev.path)
        path.append([prev.x, prev.y-1])
        return Move(x=prev.x, y=prev.y-1, maze=maze, gem=gem, path=path)
    def can_go_left(s):
        x = s.x - 1
        y = s.y
        if x < 0:
            return False
        elif s.maze[y][x] == '#' or s.maze[y][x] == 'X':
            return False
        val = s.maze[y][x]
        return not (is_gem(val) and val == s.gem)
    def can_go_right(s):
        x = s.x + 1
        y = s.y
        if x >= max_x:
            return False
        elif s.maze[y][x] == '#' or s.maze[y][x] == 'X':
            return False
        val = s.maze[y][x]
        return not (is_gem(val) and val == s.gem)
    def can_go_up(s):
        x = s.x
        y = s.y + 1
        if y >= max_y:
            return False
        elif s.maze[y][x] == '#' or s.maze[y][x] == 'X':
            return False
        val = s.maze[y][x]
        return not (is_gem(val) and val == s.gem)
    def can_go_down(s):
        x = s.x
        y = s.y - 1
        if y < 0:
            return False
        elif s.maze[y][x] == '#' or s.maze[y][x] == 'X':
            return False
        val = s.maze[y][x]
        return not (is_gem(val) and val == s.gem)
    def is_goal(move):
        return move.x == goal_x and move.y == goal_y
    def pretty_print(move):
        m = move.maze
        for y in m:
            print ''.join(y)
            
    # parse input
    for line in sys.stdin:
        max_y, max_x = line.rstrip().split()
        max_x = int(max_x)
        max_y = int(max_y)
        break;
    for line in sys.stdin:
        start_y, start_x = line.rstrip().split()
        start_x = int(start_x)
        start_y = int(start_y)
        break;
    maze = []
    for y, line in enumerate(sys.stdin):
        maze.append(list(line.rstrip()))
        if 'G' in line:
            goal_x = line.find('G')
            goal_y = y
    maze[start_y][start_x] = 'X'
    first = Move(x=start_x, y=start_y, maze=maze, gem='', path=[[start_x, start_y]])
    q = [first]
    while q:
        move = q.pop(0)
        if is_goal(move):
            move.maze[move.y][move.x] = 'X'
            pretty_print(move)
            sys.exit(0)
        if can_go_left(move):
            q.append(go_left(move))
        if can_go_right(move):
            q.append(go_right(move))
        if can_go_up(move):
            q.append(go_up(move))
        if can_go_down(move):
            q.append(go_down(move))
    print "NO SOLUTION"

