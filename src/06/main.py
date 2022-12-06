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

table = new_table(None, width=2, height=4)
tests = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
    "nppdvjthqldpwncqszvftbrmjlhg": 23,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw":  26,
}
data = None
with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    data = f.readline().strip()


WINDOW_SIZE = 14
def find_marker(string: str):
    chars = list(string)
    seen = set()
    window = []
    for i, char in enumerate(chars):

        if len(window) == WINDOW_SIZE:
            window = window[1:] + [char]
        else:
            window.append(char)

        if len(set(window)) == WINDOW_SIZE:
            return i+1


    return -1


for msg, expected in tests.items():
    print(find_marker(msg), expected)

print(find_marker(data))

