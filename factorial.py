import operator
from functools import reduce

def fact1(n: int) -> int:
    '''Implements a factorial with reduce function'''
    new_list = []
    num = n
    while num > 0:
        new_list.append(num)
        num = num - 1
    total = reduce(operator.mul, new_list)
    return total

print(f'{fact1(5)=}')


def fact2(n: int) -> int:
    '''Implements a factorial with recursion'''          # O(n!)
    if n == 1:
        return 1
    else:
        total = n * fact2(n-1)
    return total

print(f'{fact2(5)=}')

def fact3(n: int) -> int:
    '''Implements a factorial with loop'''        # most time efficient O(n)
    total = 1
    while n > 1:
        total = total * n
        n = n-1
    return total

print(f'{fact3(5)=}')
print(f'\n{"=" * 10}\n')
