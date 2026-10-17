# Problem 2:String Split and Join
# Hacker Rank Link:https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result

line = input()
print(split_and_join(line))
