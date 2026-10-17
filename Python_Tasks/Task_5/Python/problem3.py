# Problem 3:Mutations
# Hacker Rank Link:https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

s = input()
position, character = input().split()
result = mutate_string(s, int(position), character)
print(result)
