# Problem 18:Set Mutations
# Hacker rank link:https://www.hackerrank.com/challenges/py-set-mutations/problem
n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, _ = input().split()
    other = set(map(int, input().split()))
    getattr(A, operation)(other)

print(sum(A))