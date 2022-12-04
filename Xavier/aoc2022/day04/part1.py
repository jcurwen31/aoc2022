from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def a_contain_b(a, b):
    # print(a,b)
    if len(list(range(*a))) < len(list(range(*b))):
        a, b = b, a
    # print(a, b)
    return True if min(a) <= min(b) and max(a) >= max(b) else False
    
def str_to_int(elves_group):
    x, y = elves_group[0].split('-'), elves_group[1].split('-')
    x = [int(x) for x in x]
    y = [int(y) for y in y]
    return (x,y)



def compute(s: str) -> int:

    data = s.splitlines()

    elves_groups = [d.split(',') for d in data]
    elves_groups = [str_to_int(g) for g in elves_groups]

    included = sum([a_contain_b(*g) for g in elves_groups])


    return included



INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2




@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected

def test_str_to_int():
    expected = ([2, 4], [6, 8])
    assert str_to_int(['2-4', '6-8']) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
