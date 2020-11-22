#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    rps = ["rock", "paper", "scissors"]

    def inner(n):
        if n == 0:
            return []

        for p in rps:
            pass

        return inner(n - 1)

    return inner(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
