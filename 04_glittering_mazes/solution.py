#!/usr/bin/env python
import sys
import copy
from collections import namedtuple
if __name__ == '__main__':
    Move = namedtuple('Move', ['x', 'y', 'maze', 'gem'])
    def is_gem(val): return val in ('R', 'E')
    def valid(val): return val != '#' and val != 'X'    
    def helper(prev):
        loc = prev.maze[prev.y][prev.x]
        maze = copy.deepcopy(prev.maze)
        maze[prev.y][prev.x] = 'X'
        return (maze, loc if is_gem(loc) else prev.gem)
    def go_left(prev): return Move(prev.x-1, prev.y, *helper(prev))
    def go_right(prev): return Move(prev.x+1, prev.y, *helper(prev))
    def go_up(prev): return Move(prev.x, prev.y+1, *helper(prev))
    def go_down(prev): return Move(prev.x, prev.y-1, *helper(prev))
    def can_go_left(s):
        val = 'X' if s.x - 1 < 0 else s.maze[s.y][s.x - 1]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_right(s):
        val = 'X' if s.x + 1 >= max_x else s.maze[s.y][s.x + 1]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_up(s):
        val = 'X' if s.y + 1 >= max_y else s.maze[s.y + 1][s.x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    def can_go_down(s):
        val = 'X' if s.y - 1 < 0 else s.maze[s.y - 1][s.x]
        return valid(val) and not (is_gem(val) and val == s.gem)
    max_y, max_x = [int(x) for x in sys.stdin.readline().rstrip().split()]
    start_y, start_x = [int (x) for x in sys.stdin.readline().rstrip().split()] # X and Y position for starting coords are backwards
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
