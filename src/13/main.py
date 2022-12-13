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
test = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
data={1:()}
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    pair = 1
    # for idx, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data[pair] += (eval(line),)
        else:
            pair += 1
            data[pair] = ()

print(data)


def in_order(l: [int] | int, r: [int] | int):
    if type(l) == type(r) == list:
        if len(l) > 0 and len(r) > 0:
            cont = in_order(l[0], r[0])
            if cont == 'continue':
                return in_order(l[1:], r[1:])
            else:
                return cont
        return 'continue' if (len(l) == len(r)) else (len(l) < len(r))
    if type(l) == type(r) == int:
        return 'continue' if (l == r) else (l < r)
    else:
        if type(l) == int:
            return in_order([l], r)
        if type(r) == int:
            return in_order(l, [r])

        raise Exception('not possible')

pairs_in_order = []
for _id, _pair in data.items():
    left, right = _pair
    print(_id,'# '*10)
    if in_order(left, right):
        pairs_in_order.append(_id)

# print(pairs_in_order)
print('part 1:', sum(pairs_in_order))


DIV_1 = [[2]]
DIV_2 = [[6]]
data_2 = []
for left, right in data.values():
    data_2.append(left)
    data_2.append(right)
data_2 += [DIV_1, DIV_2]


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not in_order(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


bubble_sort(data_2)

idx_1 = idx_2 = 0
for idx, el in enumerate(data_2):
    if el == DIV_1:
        idx_1 = idx +1
    if el == DIV_2:
        idx_2 = idx +1

print(idx_1, idx_2, idx_1*idx_2)