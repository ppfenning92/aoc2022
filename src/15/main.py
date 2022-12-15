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

"""
row = set()
CHECK_ROW = 10
MIN_X =-25
MAX_X = 25
# CHECK_ROW = 2_000_000
# MIN_X =-2_000_000
# MAX_X = 5_000_000

for x in tqdm(range(MIN_X, MAX_X)):
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
"""

MIN_XY = 0
# MAX_XY = 20
MAX_XY = 4_000_000

# print(manhatten_distance((2,10), (8,7))) -> 9
# print(manhatten_distance((-1,7), (8,7))) -> 9


bounds = []



for s,b in data.items():
    d = manhatten_distance((s.x, s.y), (b.x, b.y))
    min_x = s.x - d
    max_x = s.x + d
    min_y = s.y - d
    max_y = s.y + d
    print((min_x, max_x), (min_y, max_y), d)
    bounds.append([
        (min_x, min_y),
        (min_x, max_y),
        (max_x, min_y),
        (max_x, max_y),
    ])


print(len(bounds))
print(bounds)

"""
               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
"""

