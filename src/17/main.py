#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re  # NOQA
import math  # NOQA
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, pairwise, combinations, combinations_with_replacement  # NOQA

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, parse_line  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8  # NOQA

import numpy as np

class Stone:
    shape: [[int]]
    falling: bool = True
    height: int
    width: int
    pos: (int, int) = (0, 2) # top-left part of stone
    def __init__(self, shape):
        self.shape = shape
        self.height = len(self.shape)
        self.width = len(self.shape[0])
    def __repr__(self):
        s = ''
        for _r in self.shape:
            for _c in _r:
                s += '#' if _c == 1 else '.'
            s += '\n'

        return s

MINUS = [[1,1,1,1]]
PLUS = [[0,1,0], [1,1,1], [0,1,0]]
L = [[0,0,1], [0,0,1], [1,1,1]]
PIPE = [[1],[1],[1],[1]]
SQUARE = [[1,1],[1,1]]

test = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
jets=[]
shapes: [[[int]]] = [MINUS, PLUS, L, PIPE, SQUARE]

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(test.split('\n')):
    # for i, line in enumerate(f):
        line = line.strip()
        jets = list(line)

print(jets)

FIELD = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
]
ROCKS = 2022

step = 0

def can_stone_fall(_stone: Stone) -> bool:
    _y, _x = _stone.pos
    if _y+_stone.height > len(FIELD)-1:
        return False
    for _c in range(len(_stone.shape[-1])):
        stone_part = _stone.shape[-1][_c]
        rr = _stone.height + _y
        cc = _c + _x - 1
        field_pos = FIELD[rr][cc]
        if stone_part == 1:
            if field_pos == '#':
                return False
    return True

def can_stone_move_left(_stone: Stone):
    _y, _x = stone.pos
    if (x - 1) < 0:
        return False
    for _r in range(len(_stone.shape)):
        for _c in range(len(_stone.shape[_r])):
            if _stone.shape[_r][_c] == 1:
                if FIELD[_r + _y][_c + _x - 1] == '#':
                    return False
    return True
def can_stone_move_right(_stone: Stone):
    _y, _x = stone.pos
    if (x + _stone.width + 1) >= 7:
        return False
    for _r in range(len(_stone.shape)):
        for _c in range(len(_stone.shape[_r])):
            if _stone.shape[_r][_c] == 1:
                if (_c + _x + 1) >= 7:
                    return False
                if (_r + _y) > len(FIELD):
                    return False
                if FIELD[_r + _y][_c + _x + 1] == '#':
                    return False
    return True
for rock in range(4):
    stone = Stone(shapes[rock % len(shapes)])

    for _ in range(stone.height):
        FIELD.insert(0,['.', '.', '.', '.', '.', '.', '.'])

    print(stone)

    while stone.falling:
        y,x = stone.pos
        jet = jets[step % len(jets)]

        if jet == '>':
            if can_stone_move_right(stone):
                x += 1

        if jet == '<':
            if can_stone_move_left(stone):
                x += -1

        for r in range(y, y + stone.height):
            for c in range(x, x + stone.width):
                FIELD[r][c] = '@' if stone.shape[r-y][c-x] == 1 else FIELD[r][c]

        print_grid(FIELD, str)
        print(y)

        if can_stone_fall(stone):
            stone.pos = (y+1,x)
        else:
            stone.falling = False
        for r_idx in range(len(FIELD)):
            for c_idx in range(len(FIELD[r_idx])):
                FIELD[r_idx][c_idx] = '.' if FIELD[r_idx][c_idx] != '#' else '#'
                if not stone.falling:
                    for r in range(y, y + stone.height):
                        for c in range(x, x + stone.width):
                            FIELD[r][c] = '#' if stone.shape[r - y][c - x] == 1 else '.'

        step += 1
