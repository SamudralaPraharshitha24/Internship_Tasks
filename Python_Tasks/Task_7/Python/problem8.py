# Problem 8:Gem stones
# Hacker Rank Link:https://www.hackerrank.com/challenges/gem-stones/problem
def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common &= set(rock)
    return len(common)

if __name__ == '__main__':
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))