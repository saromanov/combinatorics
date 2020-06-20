from typing import List, Set

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

print(subsets([4,5,2,8,9]))