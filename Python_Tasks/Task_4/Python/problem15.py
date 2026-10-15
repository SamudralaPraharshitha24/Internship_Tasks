# Problem 15: Word Order
# Hacker Rank Link:https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    words = OrderedDict()

    for i in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1

    print(len(words))
    print(*words.values())