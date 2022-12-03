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
test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


# for i, line in enumerate(test.split("\n")):
#     data.append(tuple([x for x in chunks(list(line), len(line)//2)]))
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(tuple([x for x in chunks(list(line), len(line)//2)]))


print(data)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return list(set(lst3))

items = []
for half1, half2 in data:
    inter = intersection(half1, half2)[0]
    items.append(inter)

values = list(ascii_lowercase+ascii_uppercase)
value = 0
for item in items:
    value += values.index(item) +1

print(value)


groups = [g for g in chunks(data, 3)]

items_2 = []
for group in groups:
    e1 = list([item for sublist in group[0] for item in sublist])
    e2 = list([item for sublist in group[1] for item in sublist])
    e3 = list([item for sublist in group[2] for item in sublist])

    e12 = intersection(e1,e2)
    e123 = intersection(e12,e3)
    items_2.append(e123[0])


value = 0
for item in items_2:
    value += values.index(item) +1

print(value)
