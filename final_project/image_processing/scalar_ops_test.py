#!/usr/bin/env python3

from scalar_ops import laMultiplication, laSqRoot, laSquare

test_cases = [
    (0, 0),
    (0, -1),
    (-1, 0),
    (5, 7),
    (-1, -1),
    (8, -3),
    (8, -1),
    (-8, 3),
    (-8, -3),
    (15, 1),
    (3, 3),
    (40,0),
    (16,1024)
]

for a, b in test_cases:
    result, enrg, prtime = laMultiplication(a, b)
    is_res_correct = result == a*b
    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laMultiplication({a}, {b}) = {result, enrg, prtime}, test: {is_res_correct}")

    print("\033[0m", end='')

test_cases = [0, -1, -2, 2, 6, 64, -10, 5, 16, -8, 1]

for a in test_cases:
    result,enrg, prtime = laSquare(a, nstages=5)
    is_res_correct = result == a**2

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSquare({a}) = {result,enrg, prtime}, test: {is_res_correct}")

    print("\033[0m", end='')

tst_cases = [(0,0), (1,1), (2,1), (4,2), (8,2), (16, 4), (25,5), (30,5), (35,5), (784, 28), (807, 28), (1023098, 1011)]
# tst_cases = [(784, 28)]

for tst, _ in tst_cases:
    res, enrg, prtime = laSqRoot(tst, nstages = 14)
    corr_res = int(tst ** 0.5)

    is_res_correct = res == corr_res

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSqRoot({tst}) = {res,enrg, prtime}, correct: {is_res_correct} ({corr_res})")
    print("\033[0m", end='')
