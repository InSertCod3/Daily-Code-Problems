import os
import sys

"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

T_L = [[[1, 2, 3, 4, 5], [120, 60, 40, 30, 24]], [[3, 2, 1], [2, 3, 6]]]

def _list_multiply(L):  # Avoid using numpy's easy function "numpy.prod(LIST)"
    _R = 1
    for n in L:
        _R = _R * n
    return _R

def test(I, O):
    _f = []
    for _in_pos, _in_v in enumerate(I):
        N = list(I)
        N.pop(_in_pos)
        _f.append(_list_multiply(N))
    return (True if _f == O else False, _f)
        

if __name__ == "__main__":
    for IN in T_L:
        print(test(*IN))