#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    ans = []
    plays = ["rock", "paper", "scissors"]

    def inner(n):
        if n == 0:
            ans.append([])

    inner(n)

    return ans


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
