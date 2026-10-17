# Problem 16:Check Subset
# Hacker rank Link:https://www.hackerrank.com/challenges/py-check-subset/problem
T = int(input())

for _ in range(T):
    n = int(input())
    A = set(input().split())
    m = int(input())
    B = set(input().split())
    print(A.issubset(B))