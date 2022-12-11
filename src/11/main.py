#!/usr/bin/env python

from __future__ import annotations

import os  # NOQA
import sys  # NOQA

import os, sys
import typing
from time import sleep

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.set_int_max_str_digits(1000000)
import re  # NOQA
import math  # NOQA
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, pairwise, combinations, combinations_with_replacement  # NOQA

import queue

q = queue.Queue()

from utils import chunks, gcd, lcm, print_grid, min_max_xy, parse_nums, parse_line  # , factors  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8  # NOQA

import numpy as np

total = 0
table = new_table(None, width=2, height=4)
data = []
test = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Monkey:
    id: int
    items: queue.Queue
    op: str
    test: int
    if_true: int
    if_false: int
    inspection: int

    def __init__(self, _id, items, op, _test, if_true, if_false):
        self.id = _id
        self.items = queue.Queue()
        for i in items:
            self.items.put(i)
        self.op = op
        self.test = _test
        self.if_true = if_true
        self.if_false = if_false
        self.inspection = 0

    # Part 1
    def turn(self):
        self.inspection += 1
        # get first item
        old = self.items.get()
        # apply op to item
        new = eval(self.op)
        # divide by 3 (integer div)
        new = new // 3
        return new, self.if_true if new % self.test == 0 else self.if_false

    def turn_2(self):
        self.inspection += 1
        divisors = [5, 2, 13, 7, 19, 11, 3, 17]
        # get first item from queue
        old: int = self.items.get()
        # apply operation to item
        new_oped = eval(self.op)
        # do maths magic
        new = calc_rest_class(new_oped, divisors)
        # return new value and target monkey
        return new, self.if_true if new % self.test == 0 else self.if_false

    def __repr__(self):
        return f"""Monkey {self.id}
Items: {list(self.items.queue)} 
Operation: {self.op}
Tets: {self.test}
If true: {self.if_true}
If false: {self.if_false}
"""


def prod(vals: [int]):
    res = 1
    for v in vals:
        res *= v
    return res
def calc_rest_class(n: int, divisors: [int]):
    _m = 0
    inc = set()
    while True:
        _m += prod(list(inc))
        if _m > n:
            return n
        found = True
        for d in divisors:
            if (n % d) == (_m % d):
                inc.add(d)
            else:
                found = False

        if found:
            return _m


def create_monkey_from_text(text: str):
    vals = [l.strip() for l in text.split('\n') if l.strip()]
    if len(vals) != 6:
        return
    id_str, items_str, op_str, test_str, true_str, false_str = vals

    _id = parse_nums(id_str)[0]
    items = parse_nums(items_str)
    op = op_str.split('=')[1].strip()
    _test = parse_nums(test_str)[0]
    if_true = parse_nums(true_str)[0]
    if_false = parse_nums(false_str)[0]
    return Monkey(_id, items, op, _test, if_true, if_false)


with fileinput.input(files=(f"input.txt",), encoding="utf-8") as f:
    read = ""
    # for i, line in enumerate(test.split('\n')):
    for i, line in enumerate(f):
        line = line.strip()
        read += line + '\n'

    monkeys = dict()
    for t in read.split('\n\n'):
        m = create_monkey_from_text(t)
        if m:
            monkeys[m.id] = m

rounds = 10_000
for round in range(rounds):
    for mon_id, mon in monkeys.items():
        for i in range(len(list(mon.items.queue))):
            item, target = mon.turn_2()
            monkeys[target].items.put(item)

monkey_business = []
for mon in monkeys.values():
    monkey_business.append(mon.inspection)

monkey_business.sort()
n1, n2 = monkey_business[-2:]

print(n1 * n2)
print('should be', 2713310158)
print('correct', n1 * n2 == 2713310158)
