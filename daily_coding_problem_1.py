import os
import sys


"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


T_L = [[[10, 15, 3, 7], 17], [[24, 13, 56, 26], 50], [[98, 45, 12, 122], 167]]

def test(I, O):
    for u in I:
        for s in I:
            if s + u == O:
                return True, (s, u)

if __name__ == "__main__":
    for IN in T_L:
        print(test(*IN))