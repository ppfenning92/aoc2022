#!/usr/bin/env python
from __future__ import annotations
import os  # NOQA
import sys  # NOQA

import os, sys
import time
from typing import Optional, Tuple, Literal, List

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import numpy as np

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

total = 0
result = []
table = new_table(None, width=2, height=4)
data = []
# test = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

test = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
class Knot:
    next: Knot | None
    prev: Knot | None
    pos: np.ndarray
    last_pos: np.ndarray
    def __init__(self, name, next: Knot = None, prev: Knot = None):
        self.next = next
        self.prev = prev
        self.pos = np.array([0,0])
        self.last_pos = None
        self.name = name

    def __repr__(self):
        return f"{self.name}, {self.pos}"

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
    # for i, line in enumerate(test.split('\n')):
        line = line.strip()
        if line:
            data.append(tuple(line.split(' ')))

print(data)
HEAD = Knot('head')
curr = HEAD
for p in range(8):
    k = Knot(f"{p + 1}")
    curr.prev = k
    k.next = curr
    # print(curr.next, curr, curr.prev)
    curr = k

TAIL = Knot('tail')
curr.prev = TAIL
TAIL.next = curr
# print(curr.next, curr, curr.prev)

curr = HEAD
while curr:
    # print(curr)
    curr = curr.next

START = np.array([0, 0])

tail_pos = set()
tail_pos.add((0,0))
def move(knot: Knot, d: Literal['U'] | Literal['R'] | Literal['D'] | Literal['L']):
    # knot.last_pos = knot.pos.copy()

    if d == 'U':
        knot.pos += np.array([1, 0])
    if d == 'R':
        knot.pos += np.array([0, 1])
    if d == 'D':
        knot.pos += np.array([-1, 0])
    if d == 'L':
        knot.pos += np.array([0, -1])

    curr_part: Knot = knot.prev
    while curr_part:
        # if np.linalg.norm(curr_part.pos - curr_part.next.pos) > (2 ** .5):
        #     curr_part.last_pos = curr_part.pos.copy()
        #     curr_part.pos = curr_part.next.last_pos.copy()
        #     if curr_part == TAIL:
        #         tail_pos.add(tuple(TAIL.pos))
        #
        # curr_part = curr_part.prev
        if np.linalg.norm(curr_part.pos - curr_part.next.pos) > (2 ** .5):
            if curr_part.pos[0] == curr_part.next.pos[0] and curr_part.pos[1] < curr_part.next.pos[1]:
                curr_part.pos += np.array([0,1])
            if curr_part.pos[0] == curr_part.next.pos[0] and curr_part.pos[1] > curr_part.next.pos[1]:
                curr_part.pos += np.array([0,-1])
            if curr_part.pos[0] < curr_part.next.pos[0] and curr_part.pos[1] == curr_part.next.pos[1]:
                curr_part.pos += np.array([1,0])
            if curr_part.pos[0] > curr_part.next.pos[0] and curr_part.pos[1] == curr_part.next.pos[1]:
                curr_part.pos += np.array([-1,0])
            if curr_part.pos[0] < curr_part.next.pos[0] and curr_part.pos[1] < curr_part.next.pos[1]:
                curr_part.pos += np.array([1,1])
            if curr_part.pos[0] > curr_part.next.pos[0] and curr_part.pos[1] > curr_part.next.pos[1]:
                curr_part.pos += np.array([-1,-1])
            if curr_part.pos[0] < curr_part.next.pos[0] and curr_part.pos[1] > curr_part.next.pos[1]:
                curr_part.pos += np.array([1,-1])
            if curr_part.pos[0] > curr_part.next.pos[0] and curr_part.pos[1] < curr_part.next.pos[1]:
                curr_part.pos += np.array([-1,1])

            if curr_part == TAIL:
                tail_pos.add(tuple(TAIL.pos))

        curr_part = curr_part.prev

for dir, steps in data:
    for s in range(int(steps)):
        move(HEAD, dir)
#
# move(HEAD, 'U')
# print(HEAD, TAIL)
#
#
# move(HEAD, 'U')
# print(HEAD, TAIL)
#

print(tail_pos)
print(len(tail_pos))
