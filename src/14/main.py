#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
import time
from time import sleep

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

total = 0
data=[]
test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            paths = [tuple(parse_nums(p)) for p in line.split(' -> ')]
            data.append(paths)

# print(data)
stones = []
# set stones
for points in data:
    # print([p for p in pairwise(points)])
    for p1,p2 in pairwise(points):
        if p1[0] == p2[0]:
            x = p1[0]
            it = 1 if p1[1] < p2[1] else -1
            for y in range(p1[1],p2[1] + it, it):
                stones.append((x, y))
        if p1[1] == p2[1]:
            y = p1[1]
            it = 1 if p1[0] < p2[0] else -1
            for x in range(p1[0],p2[0] + it, it):
                stones.append((x, y))


MIN_X = min([x for x,y in stones])
MAX_X = max([x for x,y in stones])
MIN_Y = 0 #min([y for x,y in cave.keys()])
MAX_Y = max([y for x,y in stones])

print(MIN_X, MAX_X, MIN_Y, MAX_Y)
# print(stones)

# WIDTH = MAX_X - MIN_X + 1
WIDTH = 500
# WIDTH = 60
cave = new_table('.', width=WIDTH, height=MAX_Y + 3)

for x,y in stones:
    cave[y][x-MIN_X + WIDTH // 2] = '#'

# for x,y in stones:
#     cave[y][x] = '#'

for c in range(WIDTH):
    cave[len(cave)-1][c] = '#'
# print_grid(cave)

## sand: 500,0
## down -> down-left -> down right
ts = time.time()
while cave[0][500 + (WIDTH // 2) - MIN_X] != '0':
    try:
        for r in range(len(cave)-1,-1,-1):
            for c in range(len(cave[r])):
                if cave[r][c] == '+':
                    # down ?
                    if cave[r+1][c] == '.':
                        cave[r+1][c] = cave[r][c]
                        cave[r][c] = '.'
                        continue
                    # down-left
                    if cave[r+1][c-1] == '.':
                        cave[r+1][c-1] = cave[r][c]
                        cave[r][c] = '.'
                        continue
                    # down-right
                    if cave[r+1][c+1] == '.':
                        cave[r+1][c+1] = cave[r][c]
                        cave[r][c] = '.'
                        continue
                    cave[r][c] = '0'

        if cave[0][500-MIN_X + WIDTH // 2] == '0':
        # if cave[0][500] == '+':
            print('this')
            break
        else:
            cave[0][500-MIN_X + WIDTH // 2] = '+'
        # cave[0][500] = '+'
    except Exception:
        break

count_sand = 0
for r in cave:
    for c in r:
        if c == '0':
            count_sand += 1

print_grid(cave)
print(count_sand)
print('took', time.time() - ts, 'seconds')
print('expected', 25248)

h = 164

