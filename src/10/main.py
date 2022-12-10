#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
from time import sleep

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
data=[]
test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data.append(line.split(' '))


checkpoint = 20
cycle = 0
X = 1
X_hist = []
table = new_table('.',width=40, height=6 )

pixels = []

for idx, inst in enumerate(data):
    val = 0
    op = inst[0]

    if len(inst) == 1:
        cycle += 1

    if len(inst) == 2:
        val = int(inst[1])


    if op == 'addx':
        for c in range(2):
            cycle += 1
            if cycle == checkpoint:
                X_hist.append(X * cycle)
                checkpoint += 40
        X += val
        val = 0

    if cycle == checkpoint:
        X_hist.append(X * cycle)
        checkpoint += 40



print('PART 1:', sum(X_hist), '\n')


crt_pos = (0,0)
sprites = [0,1,2]
cycle = 0

def get_inst():
    for _inst in data:
        yield _inst


instructions = get_inst()

inst = instructions.__next__()

execute = False
X = 1
while inst:
    op = inst[0]
    crt_pos_x, crt_pos_y = crt_pos
    print(cycle, op, execute, X, crt_pos, sprites)
    if crt_pos_x in sprites:
        try:
            table[crt_pos_y][crt_pos_x] = '#'
        except IndexError:
            print('ERROR', crt_pos)
    print_grid(table)
    print('\n')
    # sleep(.2)
    if op == 'addx':
        val = int(inst[1])
        if execute:
            X += val
            sprites = [X-1, X, X+1]
            inst = instructions.__next__()
            execute = False
        else:
            execute = True
    else:
        try:
            inst = instructions.__next__()
            execute = False
        except StopIteration:
            break

    cycle += 1
    crt_pos = (cycle % 40, (cycle // 40) % 6)
    # if cycle > 6:
    #     break






print_grid(table)
