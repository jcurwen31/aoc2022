from __future__ import annotations

import argparse
import os.path

import pytest
from collections import deque
import re
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

stacks = dict()

def execute_command(quantity, s1, s2):
    temp_stack = deque()
    for _ in range(quantity):
        temp_stack.append(stacks[s1].pop())
    for _ in range(quantity):
        stacks[s2].append(temp_stack.pop())

def compute(s: str) -> int:
    stacks_lines = []
    commands = []
    # laoding data
    data = s.splitlines()
    for l in data:
        if '[' in l:
            stacks_lines.append(l)
        if 'move' in l:
            commands.append(l)

    # initialization
    for s in stacks_lines:
        x = 0
        for i, c in enumerate(s[1:]):
            if i % 4 == 0:
                x = x+1
                stacks[x] = stacks.get(x, '') + c
    
    for i,v in stacks.items():
        stacks[i] = deque(v.replace(" ", "")[::-1])

    # executing moves
    for c in commands:
        x = [int(y) for y in re.findall('[0-9]+', c)]
        execute_command(*x)

    # collect top of stacks
    response = ""
    for k, v in stacks.items():
        response = response + v.pop() 

    return response.strip()


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = "CMZ"


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
