from __future__ import annotations

import argparse
import os.path

import pytest
from collections import deque
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def get_marker(stream):
    marker = deque()
    for i, c in enumerate(stream):
        marker.append(c)
        if len(marker) > 14:
            marker.popleft()
        if len(marker) == 14:
            if len(set(marker)) == 14:
                return i + 1
    return None

def compute(s: str) -> int:

    lines = s.splitlines()
    stream = lines[0].strip()
    # init
    result = get_marker(stream)


    return result


INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
EXPECTED = 19


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
