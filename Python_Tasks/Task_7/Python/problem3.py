# Problem 3:Mars Exploration
# Hacker Rank Link:https://www.hackerrank.com/challenges/mars-exploration/problem

import math
import os
import random
import re
import sys
def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(1 for a, b in zip(s, expected) if a != b)

if __name__ == '__main__':
    s = input().strip()
    print(marsExploration(s))