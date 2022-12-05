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

def find_common(t1, t2):
    try:
        return (set(t1) & set(t2)).pop()
    except:
        return None


def compute(s: str) -> int:
    
    rucksacks = s.split("\n")
    rucksacks = [r.strip() for r in rucksacks if len(r) > 0]
    rucksacks = [ (r[:int((len(r)/2))], r[int(len(r)/2):]) for r in rucksacks]
    
    sum_prio = 0
    x = 0
    c_items_all = []
    for r in rucksacks:
        try:
            items = list(set(r[0]).intersection(set(r[1])))
            if len(items) > 0:


                for i in items:

                    sum_prio += find_prio(i)
                    c_items_all.append(i)
            else:
                print(f'{r=}\n{x=}')        
                # pass
        except IndexError as e:
            # print(f'{r=}\n{x=}')
            continue
    
    return sum_prio


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

EXPECTED = 157


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
