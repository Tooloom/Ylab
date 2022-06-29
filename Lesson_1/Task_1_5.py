from itertools import combinations_with_replacement
from functools import reduce


def count_find_num(primesL, limit):
    base = reduce(lambda a, b: a * b, primesL)                  # first initial combination with all numbers
    mul_list = [base]

    if base > limit:
        return []
    elif base == limit:
        return [1, limit]
    else:
        for i in range(1, limit // min(primesL)):               # more like 'while True'
            break_flag = False
            for j in combinations_with_replacement(primesL, i):
                x = reduce(lambda a, b: a * b, j) * base
                if x <= limit:
                    mul_list.append(x)
                elif x > limit and set(j) == {min(primesL)}:    # exit condition
                    break_flag = True
                    break
            if break_flag:
                break

        return [len(mul_list), max(mul_list)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
