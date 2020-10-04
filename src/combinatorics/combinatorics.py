from typing import List, Set
import numpy as np

def subsets(lst:List[int]) -> List[Set[int]]:
    result = []

    def inner(current, rest):
        if rest == []:
            result.append(current)
            return

        (first, *rest) = rest
        inner(current + (first,), rest)
        inner(current, rest)

    inner((), lst)
    return result

def factorial_n(n, r):
    if r > n:
        raise Exception('r should be less or equal to n')
    d = n - r
    result = 0
    for i in range(1, d):
        result += n * (n - i)
    return result

def combinations(n, r):
    return factorial_n(n,r)/np.math.factorial(r)

def permutations(lst: List[int]) -> List[int]:
    result = []
    def inner(current, last):
        if last == []:
            result.append(current)
            return
        for r in last:
            inner(current + (r,), [i for i in last if i != r])
    inner((), lst)
    return result