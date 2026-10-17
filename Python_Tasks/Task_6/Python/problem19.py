# problem 19:Company logo
# Hacker Rank link:https://www.hackerrank.com/challenges/most-commons/problem
if __name__ == '__main__':
    from collections import Counter

s = input().strip()
counts = Counter(s)
top = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
for ch, c in top:
    print(ch, c)