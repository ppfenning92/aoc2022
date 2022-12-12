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
test = """30373
25512
65332
33549
35390"""


with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    for i, line in enumerate(f):
    # for i, line in enumerate(test.split('\n')):
        line = line.strip()
        if line:
            data.append([int(t) for t in list(line)])


WIDTH = len(data[1])
HEIGHT = len(data)
vis = 2*HEIGHT + 2*(WIDTH-2)

"""
5 5 1
5 3 3 
3 5 4
"""
# def check_vis(h, trees:[int]):
#     global  vis
#     return all(t < h for t in trees)
# def check_dir(x, y):
#     h = data[x][y]
#
#     comp = []
#     # top
#     for _x in range(x):
#         comp.append(data[_x][y])
#     if check_vis(h, comp):
#         return True
#     comp = []
#     # bot
#     for _x in range(x+1,HEIGHT):
#         comp.append(data[_x][y])
#     if check_vis(h, comp):
#         return True
#     comp = []
#     # right
#     for _y in range(y+1, WIDTH):
#         comp.append(data[x][_y])
#     if check_vis(h, comp):
#         return True
#     comp = []
#     # left
#     for _y in range(y):
#         comp.append(data[x][_y])
#     if check_vis(h, comp):
#         return True

def check_dir(x, y):
    h = data[x][y]
    t = r = b = l = 0
    comp = []
    for _x in range(x):
    # top
        comp.append(data[_x][y])
    comp.reverse()
    for c in comp:
        t += 1
        if c >= h:
            break

    comp = []
    for _x in range(x+1,HEIGHT):
    # bot
        comp.append(data[_x][y])
    for c in comp:
        b += 1
        if c >= h:
            break

    comp = []
    for _y in range(y+1, WIDTH):
    # right
        comp.append(data[x][_y])
    for c in comp:
        r += 1
        if c >= h:
            break

    comp = []
    for _y in range(y):
    # left
        comp.append(data[x][_y])
    comp.reverse()
    for c in comp:
        l += 1
        if c >= h:
            break

    print(h, '-', (t,l,b,r))
    return t * r * b * l


best = []
for i in range(1,WIDTH-1):
    for j in range(1,HEIGHT-1):
        # if check_dir(i, j):
        #     vis += 1
        best.append(check_dir(i,j))

# print(vis)
print(best)
print(max(best))



"""
3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0
"""


"""
      7   
      1   
6 5 3 3 2
      4  
      9  
"""