#!/usr/bin/env python

import os  # NOQA
import sys  # NOQA

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

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
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(int(line))

    print(data)

# increased = 0
#
# for i in range(len(data)-3):
#     try:
#         if int(data[i]) < int(data[i+1]):
#             increased += 1
#
#     except:
#         pass
#
# print(increased)

data=[int(v) if v else 0 for v in data]
chunks=[]
for i in range(len(data)-2):
    chunks.append(data[i:i+3])

# print(chunks)

sums = [sum(chunk) for chunk in chunks]
inc = 0
for i in range(len(sums)-1):
    if sums[i] < sums[i+1]:
        inc += 1


print(inc)