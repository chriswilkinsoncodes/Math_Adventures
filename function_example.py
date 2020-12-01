#!/usr/bin/env python

import math


def f(x):
    return math.sqrt(x+3) - x + 1


if __name__ == "__main__":
    print(f(0))
    print(f(1))
    print(f(math.sqrt(2)))
    print(f(math.sqrt(2)-1))
