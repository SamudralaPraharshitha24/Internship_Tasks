# Problem 19:Weighted uniform string
# Hacker rank link:https://www.hackerrank.com/challenges/weighted-uniform-string/problem
def weightedUniformStrings(s, queries):
    weights = set()
    i = 0
    while i < len(s):
        w = ord(s[i]) - ord('a') + 1
        run = 0
        j = i
        while j < len(s) and s[j] == s[i]:
            run += 1
            weights.add(w * run)
            j += 1
        i = j
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input().strip()
    n = int(input())
    queries = [int(input()) for _ in range(n)]
    for ans in weightedUniformStrings(s, queries):
        print(ans)