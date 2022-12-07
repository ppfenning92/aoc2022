#!/usr/bin/env python
from __future__ import  annotations
import os  # NOQA
import sys  # NOQA

import os, sys
from dataclasses import dataclass
from typing import Optional

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

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

commands = []
stdout = []
@dataclass
class FT:
    type: str
    name: str
    size: int
    parent: Optional[FT]
    children: [FT]


ft = FT(name="/", type="dir", size=0, parent=None, children=[])
current = ft
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    parse_stdout = False
    for i, line in enumerate(f):
    # for i, line in enumerate(test.split('\n')):
        line = line.strip()
        if line.startswith('$'):
            parse_stdout = False
            cmd = line.split(' ')
            if cmd[1] == 'ls':
                parse_stdout = True
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current = current.parent
                else:
                    for d in current.children:
                        if d.name == cmd[2]:
                            current = d
        else:
            size_dir, name = line.split(' ')
            if size_dir == 'dir':
                current.children.append(FT(name=name, type='dir', size=0, parent=current, children=[]))
            else:
                current.children.append(FT(name=name, type='file', size=int(size_dir), parent=current, children=[]))


total_size = 0
def calc_sizes(_ft: FT):
    global  total_size
    if len(_ft.children) > 0:
        for ch in _ft.children:
            if ch.type == 'dir':
                calc_sizes(ch)
                # print(ch.type, ch.name, _ft.size)
            else:
                total_size += ch.size
            _ft.size += ch.size

calc_sizes(ft)

print(ft)
dirs = []
def walk(_ft):
    if len(_ft.children) > 0:
        for ch in _ft.children:
            if ch.type == 'dir':
                if ch.size <= 100_000:
                    dirs.append(ch.size)
                walk(ch)

walk(ft)
print(len(dirs))

print(sum(dirs))


to_del = []
TOTAL_SPACE=70_000_000
CURRENT_SPACE=TOTAL_SPACE-total_size
NEED_FREE=30_000_000-CURRENT_SPACE


checked = set()
def find_all(_ft):
    checked.add(_ft.name)
    if len(_ft.children) > 0:
        size = 0
        for ch in _ft.children:
            size += ch.size
        if size >= NEED_FREE:
            to_del.append(_ft)
            for ch in _ft.children:
                if ch.type == 'dir' and ch.name not in checked:
                    find_all(ch)

find_all(ft)

to_del_dir = ft
for d in to_del:
    if d.size < to_del_dir.size:
        to_del_dir = d
print("\n\n", NEED_FREE,  to_del_dir)