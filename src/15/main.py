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
MAX_XY = 20
# MAX_XY = 4_000_000

# print(manhatten_distance((2,10), (8,7))) -> 9
# print(manhatten_distance((-1,7), (8,7))) -> 9


def square_spacing(s1, d1, s2, d2):
    return abs(s1[0] - s2[0]) - (d1 + d2) + abs(s1[1] - s2[1])

def overlapping_squares(s1, d1, s2, d2) -> bool:
    return square_spacing(s1, d1, s2, d2) <= 0

def line_from_adjacent_squares(s1, d1, s2, d2):
    p1 = s1[0], s1[1]+d1+1
    p2 = s2[0], s2[1]-d2-1
    p3 = s1[0], s1[1]-d1-1
    p4 = s2[0], s2[1]+d2+1
    l1 = line_from_points(p1, p2)
    l2 = line_from_points(p3, p4)
    if abs(l1[0]) == 1.0:
        return l1
    else:
        return l2

def line_from_points(p1, p2):
    A = np.array([[p1[0], 1],
                  [p2[0], 1]])
    b = np.array([p1[1], p2[1]])
    return np.rint(np.linalg.solve(A, b)).astype(int)

def line(x, m, c):
    return m*x + c

def solve_crossing_lines(l1, l2):
    A = np.array([[-l1[0], 1],
                  [-l2[0], 1]])
    b = np.array([l1[1], l2[1]])
    return np.rint(np.linalg.solve(A, b)).astype(int)

def solve_part_2() -> int:
    pairings = ((0,1,2,3),
                (0,2,1,3),
                (0,3,1,2))
    signal_distance_pairs = []
    for s, b in data.items():
        signal_distance_pairs.append(((s.x,s.y), manhatten_distance((s.x,s.y), (b.x,b.y))))

    for four_squares in combinations(signal_distance_pairs, 4):
        for p in pairings:
            i, j, k, l = [four_squares[n] for n in p]
            sep = []
            possible = False
            sep.append(square_spacing(*i, *j))
            sep.append(square_spacing(*k, *l))
            if sep == [2,2]:
                overlaps = []
                overlaps.append(overlapping_squares(*i, *k))
                overlaps.append(overlapping_squares(*i, *l))
                overlaps.append(overlapping_squares(*j, *k))
                overlaps.append(overlapping_squares(*j, *l))
                if np.all(overlaps):
                    l1 = line_from_adjacent_squares(*i, *j)
                    l2 = line_from_adjacent_squares(*k, *l)
        else:
            continue
    x, y = solve_crossing_lines(l1, l2)
    solution = 4000000*x + y
    return solution

print(solve_part_2())
"""
# combinations('ABCD', 2)                     AB AC AD BC BD CD

Each sensor + beacon pair defines a square of points that cannot contain the distress beacon.,

Assume that we are looking for a single point that is bounded by four squares.

This means that we want to find a set of four squares where:

We have two pairs of squares with a separation of 2.

All other combinations of squares have a separation of 0 or overlap (separation is negative).

Loop over all combinations of 4 squares, until we find a set of 4 squares that fit the criteria above.

Generate a pair of lines that run between each pair of squares.

Compute the point where these cross.


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

