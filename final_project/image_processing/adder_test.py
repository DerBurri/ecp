#!/usr/bin/env python3

from adder_definitions import multiBitAdder

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
]

for a, b in test_cases:
    result,enrg = multiBitAdder(a, b)
    print(f"multiBitAdder({a}, {b}) = {result,enrg}, test: {result == a+b}")
