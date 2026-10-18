# Problem 2:The captains room
# Hacker Rank Link:https://www.hackerrank.com/challenges/py-the-captains-room/problem
k = int(input())
rooms = list(map(int, input().split()))
print((k * sum(set(rooms)) - sum(rooms)) // (k - 1))