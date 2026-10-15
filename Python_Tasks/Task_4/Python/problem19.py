# Problem 19 : Collection Counter
# Hacker Rank Link:https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))

    shoe_count = Counter(shoe_sizes)

    N = int(input())
    total_earned = 0

    for i in range(N):
        size, price = map(int, input().split())

        if shoe_count[size] > 0:
            total_earned += price
            shoe_count[size] -= 1

    print(total_earned)