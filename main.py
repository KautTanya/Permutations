"""Permutations"""


def permutations(lst):
    """Permutations"""
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            min_lst = lst[:i] + lst[i + 1:]
            for new_lst in permutations(min_lst):
                yield [lst[i]] + new_lst


for j in permutations([1, 2, 3]):
    print(j)
