#!/usr/bin/env python

import math


def f(x):
    return math.sqrt(x+3) - x + 1


if __name__ == "__main__":
    for x in [0, 1, math.sqrt(2), math.sqrt(2)-1]:
        print(f(x))
