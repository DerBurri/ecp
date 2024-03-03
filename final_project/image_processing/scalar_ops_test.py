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
    result,enrg = laMultiplication(a, b)
    print(f"laMultiplication({a}, {b}) = {result, enrg}, test: {result == a*b}")

test_cases = [0, -1, -2, 2, 6, 64, -10, 5, 16, -8, 1]

for a in test_cases:
    result,enrg = laSquare(a, nbits=16)
    print(f"laSquare({a}) = {result,enrg}, test: {result == a**2}")

tst_cases = [(0,0), (1,1), (2,1), (4,2), (8,2), (16, 4), (25,5), (30,5), (784, 28), (807, 28)]
# tst_cases = [(784, 28)]

for tst, _ in tst_cases:
   res, enrg = laSqRoot(tst, nbits = 21)
   corr_res = int(tst ** 0.5)
   print(f"laSqRoot({tst}) = {res,enrg}, correct: {res == corr_res} ({corr_res})")
