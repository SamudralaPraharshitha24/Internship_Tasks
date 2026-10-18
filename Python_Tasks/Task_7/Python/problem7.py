# Problem 7:Alphabet rangoli
# Hacker Rank Link:https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    for i in range(size):
        half = [letters[size - 1 - j] for j in range(i + 1)]
        row = "-".join(half + half[-2::-1])
        lines.append(row.center(width, "-"))
    for line in lines + lines[-2::-1]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)