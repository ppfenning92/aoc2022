#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
from functools import cache

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
test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

class Valve:
    name: str
    rate: int
    open: bool
    neighbours: [Valve]

    def __init__(self, name: str, rate: int):
        self.name = name
        self.rate = rate
        self.open = False
        self.neighbours = [self]
    def __repr__(self):
        return f"Valve {'o' if self.open else 'x'} {self.name}/{self.rate} -> {[v.name for v in self.neighbours]}"

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.rate < other.rate

data={}
tunnels = {}
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            inp = line.split(' ')
            name = inp[1]
            rate = parse_nums(inp[4])[0]
            tunnels[name] = [n.replace(',', '') for n in inp[9:]]
            data[name] = Valve(name, rate)

print(tunnels)

for valve, neigh in tunnels.items():
    v = data[valve]
    v.neighbours = [data[n] for n in neigh]

interval = 1

@cache
def part1(valve: Valve, time, visited):
    if time <= 0:
        return 0
    pressure = 0
    for node in valve.neighbours:
        pressure = max(pressure, part1(node, time-1, visited))
    if valve not in visited and valve.rate > 0:
        visited = tuple(sorted([*visited, valve]))
        pressure = max(pressure, part1(valve, time - 1, visited) + valve.rate * (time - 1))
    return pressure
print(part1(data['AA'], 30, ()))


# for path in find_all_paths(data['AA'], 10, {}):
#     print(len(path),[p.name for p in path])

