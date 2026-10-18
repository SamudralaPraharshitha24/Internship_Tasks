# Problem 15:Games of thrones
# Hacker rank link:https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter

def gameOfThrones(s):
    odd = sum(1 for count in Counter(s).values() if count % 2 == 1)
    if odd <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))