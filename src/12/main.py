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

total = 0
table = new_table(None, width=2, height=4)
data=[]
test = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(list(line))

# data = np.array(data)
# START = np.array([-1,-1])
START = [-1,-1]
# END = np.array([-1,-1])
END = [-1,-1]
MAX_ROW = len(data)
MAX_COL = len(data[1])
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if col == 'S':
            START = np.array([r,c])
            data[r][c] = 'a'
        if col == 'E':
            END = np.array([r,c])
            data[r][c] = 'z'

# print_grid(data)
def diff_chars(c1,c2):
    return math.fabs(ord(c1) - ord(c2))

# WAY TO SLOW... just use some hacky dijkstra from the web and let chatGPT help:D
#
# current_pos = START.copy()
# paths = []
# visited = set()
# shortest_path = list('.'*1_000_000)
# calls = 0
# def find_paths(_from, _to, _path: []):
#     global shortest_path
#     global calls
#     calls += 1
#     if calls % 1000 == 0:
#         print(shortest_path)
#     if tuple(_from) == tuple(_to):
#         if len(_path) <= len(shortest_path):
#             shortest_path = _path.copy()
#     else:
#         _path.append((_from[0],_from[1]))
#         if len(_path) > len(shortest_path):
#             return
#         curr_r, curr_c = _from
#         for r,c in [(1,0),(0,1),(-1,0),(0,-1)]:
#             new_r, new_c = curr_r + r, curr_c + c
#             if 0 <= new_r < MAX_ROW and 0 <= new_c < MAX_COL:
#                 if diff_chars(data[curr_r][curr_c], data[new_r][new_c]) in [0,1] and (new_r, new_c) not in _path:
#                     find_paths([new_r, new_c], _to.copy(), _path.copy())
#
#
# find_paths(current_pos.copy(), END.copy(), [])

#
# print('PART 1 # '*10)
# print(len(shortest_path), "".join([data[x][y] for x,y in shortest_path]))

# PART 1
q = deque()
q.append((0, START[0], START[1]))

vis = {(START[0], START[1])}

while q:
    d, r, c = q.popleft()
    for new_row, new_col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if new_row < 0 or new_col < 0 or new_row >= len(data) or new_col >= len(data[0]):
            continue
        if (new_row, new_col) in vis:
            continue
        if ord(data[new_row][new_col]) - ord(data[r][c]) > 1:
            continue
        if new_row == END[0] and new_col == END[1]:
            print("Part 1:",d + 1)
            break
        vis.add((new_row, new_col))
        q.append((d + 1, new_row, new_col))

# PART 2
q = deque()
q.append((0, END[0], END[1]))

vis = {(END[0], END[1])}
found = False
while q and not found:
    d, r, c = q.popleft()
    for new_row, new_col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if new_row < 0 or new_col < 0 or new_row >= len(data) or new_col >= len(data[0]):
            continue
        if (new_row, new_col) in vis:
            continue
        if ord(data[new_row][new_col]) - ord(data[r][c]) < -1:
            continue
        if data[new_row][new_col] == "a":
            print("Part 2:", d + 1)
            found = True
            break
        vis.add((new_row, new_col))
        q.append((d + 1, new_row, new_col))
