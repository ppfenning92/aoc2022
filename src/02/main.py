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

map = {
    "AX": 1+3,
    "AY": 2+6,
    "AZ": 3+0,
    "BX": 1+0,
    "BY": 2+3,
    "BZ": 3+6,
    "CX": 1+6,
    "CY": 2+0,
    "CZ": 3+3,
}

print (map)
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            # data.append(int(line))
            data.append({"line": i, "value": line.split()})

sum=0
for match in data:
    sum += map["".join(match['value'])]

print('sum', sum)




mod_sum = 0
for match in data:
    elf = match['value'][0]
    target = match['value'][1]

    # lose
    if target == "X":
        if elf == "A":
            mod_sum += 3
        if elf == "B":
            mod_sum += 1
        if elf == "C":
            mod_sum += 2

    # draw
    if target == "Y":
        mod_sum += 3
        if elf == "A":
            mod_sum += 1
        if elf == "B":
            mod_sum += 2
        if elf == "C":
            mod_sum += 3
    # win
    if target == "Z":
        mod_sum += 6
        if elf == "A":
            mod_sum += 2
        if elf == "B":
            mod_sum += 3
        if elf == "C":
            mod_sum += 1


print('part2 ', mod_sum)