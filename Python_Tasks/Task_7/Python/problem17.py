# Problem 17:separate the numbers
# Hacker rank link:https://www.hackerrank.com/challenges/separate-the-numbers/problem
def separateNumbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = s[:length]
        if first[0] == '0':
            break
        x = int(first)
        built = first
        nxt = x
        while len(built) < len(s):
            nxt += 1
            built += str(nxt)
        if built == s:
            print("YES", first)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        separateNumbers(input().strip())