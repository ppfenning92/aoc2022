#!/usr/bin/env python

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

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD


total = 0
result = []
table = new_table(None, width=2, height=4)
data=[]
test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
    # for i, line in enumerate(test.split("\n")):
        line = line.strip()
        if line:
            ranges = line.split(',')
            print(ranges)
            r1 = parse_nums(ranges[0], False)
            r2 = parse_nums(ranges[1], False)
            ass1 = set(list(range(r1[0], r1[1]+1)))
            ass2 = set(list(range(r2[0], r2[1]+1)))
            data.append((ass1,ass2))

print(data)

res = 0
for a1, a2 in data:
    if a1.issubset(a2) or a2.issubset(a1):
        res += 1

print('res1', res)


overlaps = 0
for a1, a2 in data:
    if a1.intersection(a2) or a2.intersection(a1):
        overlaps += 1

print('overlaps', overlaps)
