import os
import sys

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
"""


def cdr(_cons_pair):
    '''Return The second/right argument in function input.
    - When [_cons_pair]("<function cons.<locals>.pair>") is passed, _cons_pair(right) is then given the argument
    right() ("<function cdr.<locals>.right>"), Then "<function cons.<locals>.pair>"
    runs "f()" (<-- Which is really ""<function cdr.<locals>.right>"") and returns b.
    
    Arguments:
        _cons_pair {cons()} -- Function object cons(a, b)
    
    Returns:
        int --  # return right argument / b
    '''
    
    def right(a, b):
        return b
    return _cons_pair(right)

def car(_cons_pair):
    '''Return The first/left argument in function input.
    - When [_cons_pair]("<function cons.<locals>.pair>") is passed, _cons_pair(left) is then given the argument
    left() ("<function car.<locals>.left>"), Then "<function cons.<locals>.pair>"
    runs "f()" (<-- Which is really ""<function car.<locals>.left>"") and returns a.
    
    Arguments:
        _cons_pair {cons()} -- Function object cons(a, b)
    
    Returns:
        int --  # return left argument / a
    '''
    def left(a, b):
        return a  # return left argument / a
    return _cons_pair(left)


def cons(a, b):
    """
    a, b argument input
    
    Arguments:
        a {int} -- First Argument
        b {int} -- Second Argument
    
    Returns:
        [cons.pair] -- returns pair function
    """

    def pair(f):
        return f(a, b)
    return pair

if __name__ == "__main__":
    print(cons(3, 4))
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
