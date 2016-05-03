#!/usr/bin/env python

import sys

class State(object):
    def __init__(self, board, x, y, count):
        self.board = board
        self.x = x
        self.y = y
        self.count = count
        self.myhash = hash(str(self.board))
    def __hash__(self):
        return self.myhash
    def __eq__(self, other):
        return self.myhash == other.myhash

def print_solution(state):
    board = state.board
    dim = len(board)
    for i in range(dim):
        print ','.join(str(x) for x in board[i])
    print ''

if __name__ == '__main__':
    def valid_diag(board, x0, y0):
        x = x0
        y = y0
        while x >= 0 and y < dim:
            if board[y][x]: return False
            x -= 1
            y += 1
        x = x0
        y = y0
        while x >= 0 and y >= 0:
            if board[y][x]: return False
            x -= 1
            y -= 1
        x = x0
        y = y0
        while x < dim and y < dim:
            if board[y][x]: return False
            x += 1
            y += 1
        x = x0
        y = y0
        while x < dim and y >= 0:
            if board[y][x]: return False
            x += 1
            y -= 1
        return True

    def valid_knight(board, x, y):
        def t(x0, y0):
            return (x0 < 0 or x0 >= dim or y0 < 0 or y0 >= dim) or not board[y0][x0]
        return (t(x-1,y+2) and 
                t(x-2,y+1) and  
                t(x-2,y-1) and 
                t(x-1,y-2) and  
                t(x+1,y-2) and 
                t(x+2,y-1) and 
                t(x+2,y+1) and 
                t(x+1,y+2))

    def valid(state, x, y):
        if not (x >= 0 and x < dim and y >= 0 and y < dim):
            return False
        elif state.board[y][x]:
            return False
        else:
            return valid_diag(state.board, x, y) and valid_knight(state.board, x, y)

    # init values
    dim = int(sys.stdin.readline().rstrip())
    board = [[0 for _ in range(dim)] for _ in range(dim)]
    q = set()

    # add init states
    for i in range(dim):
        for j in range(dim):
            b = [row[:] for row in board]
            b[j][i] = 1
            q.add(State(board=b, x=i, y=j, count=1))

    # bfs
    solutions = set()
    while q:
        state = q.pop()
        if state.count > dim:
            raise Exception('This should never happen!')
        elif state.count == dim:
            solutions.add(state)
        else:
            for i in range(dim):
                for j in range(dim):
                    if valid(state, i, j):
                        b = [row[:] for row in state.board]
                        b[j][i] = 1
                        q.add(State(board=b, x=i, y=j, count=state.count+1))

    print len(solutions)

