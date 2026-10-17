# Problem 9:Word Order
# Hacker Rank Link:https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

words = {}

for i in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())
