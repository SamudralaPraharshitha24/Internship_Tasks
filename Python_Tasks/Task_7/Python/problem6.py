# Problem 6:Pangrams
# Hacker Rank Link:https://www.hackerrank.com/challenges/pangrams/problem
def pangrams(s):
    letters = set(s.lower()) - {" "}
    if len(letters) == 26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))