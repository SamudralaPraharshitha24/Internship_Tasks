# Problem 14:Set Intersection operation
# Hacker rank Link:https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))