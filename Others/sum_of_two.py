# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

"""
Given two int arrays a and b, and a target int
Find if it's possible to sum up a value from each array that equals the target

e.g.
a = [1, 2, 3, 0, -100]
b = [0, -30, -200, 8]
target = 10

Ans: True (2 + 8 == 10)
"""

a = [1, 2, 3, 0, -100]
b = [0, -30, -200, 8]
target = -28

def brute_force(a, b, target):
    # remove duplicates
    a, b = list(set(a)), list(set(b))

    # loop
    for i in range(len(a)):
        complement = target - a[i]
        for j in range(len(b)):
            if b[j] == complement:
                return True
    
    return False

print(brute_force(a, b, target))

def complements_memoization(a, b, target):
    complements = set()
    for i in a:
        complements.add(target - i)
    return True if complements.intersection(set(b)) else False

print(complements_memoization(a, b, target))

def another_fast_solution(a, b, target):
    return any([target - i in b for i in a])

print(another_fast_solution(a, b, target))