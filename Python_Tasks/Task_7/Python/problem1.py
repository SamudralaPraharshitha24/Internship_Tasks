# Problem 1:set symmetric difference operation
# Hacker Rank Link:https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

print(len(english.symmetric_difference(french)))