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


stacks=[]
data=[]
test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    stack = True
    for i, line in enumerate(f):
    # for i, line in enumerate(test.split('\n')):
        line = line.strip('\n')
        if line == '':
            stack = False
            continue
        if not stack:
            l = parse_nums(line)
            Move = namedtuple('Move', ['m', 'f', 't'] )
            data.append(Move(m=l[0], f=l[1], t=l[2]))
            continue
        if stack:
            line = re.sub(r'[\[\]]', '', line)
            line = re.sub(r'\s{4}', ' ', line)
            line = line.split(' ')
            print(line)
            stacks.insert(0, [x  if x != '' else None for x in line])

    stacks = stacks[1:][::-1]
def stack_print():
    for stack in stacks:
        print(stack)

stacks = rotated(stacks)
stack_print()

for stack in range(len(stacks)):
    stacks[stack] = [x for x in stacks[stack] if x]
# PART 1
# for move, inst in enumerate(data):
#     _move, _from, _to = inst
#     print(f"\nmove {_move} from {_from} to {_to}")
#     stack_print()
#     for m in range(_move):
#         stack = stacks[_from-1]
#         crate = stack.pop()
#         stacks[_to-1].append(crate)
#
#     print('step', move)
#     stack_print()
#
# skyline = []
#
# for stack in stacks:
#     skyline.append(stack.pop())
#
# print("".join(skyline))



for move, inst in enumerate(data):
    _move, _from, _to = inst
    print(f"\nmove {_move} from {_from} to {_to}")
    stack_print()
    crates = []
    for m in range(_move):
        crates.append(stacks[_from-1].pop())

    stacks[_to-1] += crates[::-1]

    print('step', move)
    stack_print()

skyline = []

for stack in stacks:
    skyline.append(stack.pop())

print("".join(skyline))
