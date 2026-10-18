# problem 14:Anagrams
# hacker rank Link:https://www.hackerrank.com/challenges/anagram/problem
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    c1 = Counter(s[:mid])
    c2 = Counter(s[mid:])
    return sum((c1 - c2).values())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(anagram(s))