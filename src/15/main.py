#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys

from tqdm import tqdm

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
test = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
Coord = namedtuple('Coord', field_names=['x', 'y', 'type'])
data = {}
m = set()
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            sx, sy, bx, by = parse_nums(line, True)
            m.add(Coord(sx, sy, 'S'))
            m.add(Coord(bx, by, 'B'))
            data[Coord(sx, sy, 'S')] = Coord(bx, by, 'B')

from scipy.spatial.distance import cityblock as manhatten_distance

# print(manhatten_distance((2,10), (8,7))) -> 9
# print(manhatten_distance((-1,7), (8,7))) -> 9
# def all_coords_within_distance(from_coord: Coord, d: int):
#     min_x = from_coord.x - d
#     max_x = from_coord.x + d
#     min_y = from_coord.y - d
#     max_y = from_coord.y + d
#     print((min_x, max_x), (min_y, max_y), d)
#     for x in range(min_x, max_x +1):
#         for y in range(min_y, max_y +1):
#             if Coord(x,y,'S') not in m and Coord(x,y,'B') not in m and Coord(x,y,'#') not in m:
#                 if manhatten_distance((from_coord.x,from_coord.y), (x,y)) <= d:
#                     m.add(Coord(x,y,'#'))
#
#
# for s, b in data.items():
#     all_coords_within_distance(s, manhatten_distance((s.x, s.y), (b.x, b.y)))

CHECK_ROW = 2_000_000
# CHECK_ROW = 10
row = set()
# for c in m:
#     if c.y == CHECK_ROW and c.type == '#':
#         row.add(c)


MIN_X = math.inf
MAX_X = 0

for s,b in data.items():
    if s.y == CHECK_ROW or b.y == CHECK_ROW:
        x = min(s.x,b.x)
        MIN_X = x if x < MIN_X else MIN_X
        x = max(s.x, b.x)
        MAX_X = x if x > MAX_X else MAX_X


print(MIN_X, MAX_X)
for x in tqdm(range(-2_000_000, 5_000_000)):
    candidate = (x,CHECK_ROW)
    for s,b in data.items():
        dist = manhatten_distance((s.x,s.y), (b.x,b.y))
        if (x == s.x and CHECK_ROW == s.y) or (x == b.x and CHECK_ROW == b.y):
            continue
        if manhatten_distance((s.x,s.y), candidate) <= dist:
            row.add(candidate)
            break

row = list(row)
row.sort()

print(len(row))

# MULTIPLIER = 20
MULTIPLIER = 4_000_000

MIN_XY = 0
MAX_XY = 20
# MAX_XY = 4_000_000
def get_freq(_x,_y):
    return _x * MULTIPLIER + _y



