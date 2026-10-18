# Problem 12:Making anagrams
# Hacker Rank Link:https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = sum((c1 & c2).values())
    return len(s1) + len(s2) - 2 * common

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(makingAnagrams(s1, s2))