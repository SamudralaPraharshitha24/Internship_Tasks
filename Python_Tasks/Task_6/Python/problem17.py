# Problem 17:Check strict superset
# Hacker rank Link:https://www.hackerrank.com/challenges/py-check-strict-superset/problem
A = set(input().split())
n = int(input())

result = True
for _ in range(n):
    other = set(input().split())
    if not A > other:
        result = False

print(result)