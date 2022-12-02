from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


map = {
    "X": "L",
    "Y": "D",
    "Z": "W"
}

shape_gain = {
    "A": 1,
    "B": 2,
    "C": 3,
}

result_gain = {
    "L": 0,
    "D": 3,
    "W": 6
}

def result_round(p1, p2):
    p2 = map[p2]
    choices =["A", "B", "C"]
    if p1 == p2:
        return "D"
    if p1 == choices[choices.index(p2)-1]:
        result = "W"

        return result
    return "L"

def shape_to_choose(p1, p2):
    choices =["A", "B", "C"]

    p2 = map[p2]
    if p2 == "D":
        shape = p1
    elif p2 == "L":
        shape = choices[choices.index(p1)-1]
    elif p2 == "W":
        shape = choices[(choices.index(p1)+1)%3 ]

    return shape

def compute(s: str) -> int:

    total_gain = 0

    lines = s.splitlines()
    for line in lines:
        round =  line.split()
        shape = shape_to_choose(*round)
        total_gain += shape_gain[shape] + result_gain[map[round[1]]]   
    
    return total_gain


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


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
