#! /usr/bin/python
"""
Guardian article: http://goo.gl/EUSo17
- Can you do the maths puzzle for Vietnamese eight-year-olds
that has stumped parents and teachers?

- All you need to do is place the digits from 1 to 9 in the the grid.
Easy, right?

- Walk in the park.

./snake_puzzle.py
Number of solutions: 20
(3, 2, 1, 5, 4, 7, 8, 9, 6)
(3, 2, 1, 5, 4, 7, 9, 8, 6)
(5, 2, 1, 3, 4, 7, 8, 9, 6)
(5, 2, 1, 3, 4, 7, 9, 8, 6)
(5, 3, 1, 7, 2, 6, 8, 9, 4)
(5, 3, 1, 7, 2, 6, 9, 8, 4)
(5, 4, 1, 9, 2, 7, 3, 8, 6)
(5, 4, 1, 9, 2, 7, 8, 3, 6)
(5, 9, 3, 6, 2, 1, 7, 8, 4)
(5, 9, 3, 6, 2, 1, 8, 7, 4)
(6, 3, 1, 9, 2, 5, 7, 8, 4)
(6, 3, 1, 9, 2, 5, 8, 7, 4)
(6, 9, 3, 5, 2, 1, 7, 8, 4)
(6, 9, 3, 5, 2, 1, 8, 7, 4)
(7, 3, 1, 5, 2, 6, 8, 9, 4)
(7, 3, 1, 5, 2, 6, 9, 8, 4)
(9, 3, 1, 6, 2, 5, 7, 8, 4)
(9, 3, 1, 6, 2, 5, 8, 7, 4)
(9, 4, 1, 5, 2, 7, 3, 8, 6)
(9, 4, 1, 5, 2, 7, 8, 3, 6)

"""

__author__ = 'Steven Op de beeck <steven@opdebeeck.org>'

import itertools, inspect

def divide(a, b):
    if a % b == 0:
        result = a / b
    else:
        result = float('NaN')
    return result

if __name__ == '__main__':
    expr = lambda (a, b, c, d, e, f, g, h, i): \
        a + divide(13.0 * b, c) \
        + d + (12.0 * e) - f - 11 \
        + divide(g * h,float(i)) - 10 \
        == 66
    nargs_expr = len(inspect.getargspec(expr).args[0])

    numbers = range(1,10)
    solutions = []
    for p in itertools.permutations(numbers,nargs_expr):
        if expr(p):
            solutions += [p]

    print "Number of solutions:", len(solutions)
    for s in solutions:
        print s