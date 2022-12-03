from __future__ import annotations

import argparse
import os.path

import pytest

import support
from string import ascii_lowercase, ascii_uppercase

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def find_prio(item):
    priorities = list(range(1,53))
    items = ascii_lowercase + ascii_uppercase
    return priorities[items.index(item)]

def find_common(t1, t2, t3):
    try:
        return (set(t1) & set(t2) & set(t3)).pop()
    except:
        return None

def chunck(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]



def compute(s: str) -> int:
    
    rucksacks = s.split("\n")
    rucksacks = [r.strip() for r in rucksacks if len(r) > 0]
    elves_groups = list(chunck(rucksacks, 3))
    
    sum_prio = 0
    badges = []
    for g in elves_groups:
        b = find_common(*g)
        badges.append(b)
    
    prios = [find_prio(b) for b in badges]
    sum_prio = sum(prios)
    
    return sum_prio


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

EXPECTED = 70


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
