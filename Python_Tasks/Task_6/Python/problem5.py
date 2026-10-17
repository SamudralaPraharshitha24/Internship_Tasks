# Problem 5:Write a Function
# Hacker Rank link:https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

    
    return leap

year = int(input())