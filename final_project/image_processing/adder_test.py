#!/usr/bin/env python3

from adder_definitions import multiBitAdder
from random import randint

test_cases = [
    (0, 0),     # 0 + 0 = 0
    (0, -1),     # 0 + -1 = -1
    (-1, 0),     # -1 + 0 = 0
    (5, 7),     # 5 + 7 = 12
    (-1, -1),   # -1 + -1 = -2 (overflow)
    (8, -3),    # 8 + (-3) = 5
    (-8, 3),    # -8 + 3 = -5
    (-8, -3),   # -8 + (-3) = -11
    (15, 1),    # 15 + 1 = -16 (overflow)
    (-15, 1),    # 15 + 1 = -16 (overflow)
    (-4086, 512),
    (-128, 512),
    (512, -512),
]

def tst_adder(a,b, nstages = 4):
    result,enrg,prtime = multiBitAdder(a, b, nstages)
    is_res_correct = result == a+b

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"multiBitAdder({a}, {b}) = {result,enrg,prtime}, test: {is_res_correct}")

    print("\033[0m", end='')

for a, b in test_cases:
    tst_adder(a,b,5)

for _ in range(100):
    a = randint(-100, 100)
    b = randint(-100, 100)
    tst_adder(a,b)

for _ in range(100):
    a = randint(2048, 4095)
    b = randint(2048, 4095)
    tst_adder(a,b)
