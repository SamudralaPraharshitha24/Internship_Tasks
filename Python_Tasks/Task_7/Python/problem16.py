# Problem 16:Caesar cipher
# Hacker rank link:https://www.hackerrank.com/challenges/caesar-cipher-1/problem
def caesarCipher(s, k):
    k %= 26
    result = []
    for ch in s:
        if ch.islower():
            result.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif ch.isupper():
            result.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    print(caesarCipher(s, k))