#!/usr/bin/env python3
# coding: utf-8

# # Scalar functions
#
# Author: Vladislav Valek
#
# These are designed for specific applications that use multiBitAdder

# ## Reduction sum
# This function takes a 1D or 2D array of number and adds all its elements together. It uses MyNbitAdder for addition. This functionality as also known as folding.

from adder_definitions import multiBitAdder

# ## Multiplication
#
# It hurts, but it has to be done. These just accept single integer numbers.

# In[35]:

def laMultiplication(a, b, nbits = 12, approx_until = 0):
    """This accepts two parameters and performs artificial multiplication
    by successive addition."""

    # An identity value for multiplication is normally 1 but since this
    # multiplication is done by successive addition, the sum identity is taken
    # instead.
    res = 0
    total_energy = 0
    # a = a.astype(int)
    # b = a.astype(int)

    if (a == 0 or b == 0):
        return 0, 0

    # Negative numbers have to be converted to the positive but the sign
    # has to remain for the result.
    neg_res_flag = True if ((a < 0 and b > 0) or (a > 0 and b < 0)) else False

    if a < 0:
        a, enrg = multiBitAdder(0,-a, nbits = nbits, approx_until = approx_until)
        total_energy += enrg

    if b < 0:
        b, enrg = multiBitAdder(0,-b, nbits = nbits, approx_until = approx_until)
        total_energy += enrg

    for _ in range(b):
        res, energy = multiBitAdder(res,a, nbits = nbits, approx_until = approx_until)
        total_energy += energy

    if neg_res_flag:
        res *= -1

    return res, total_energy


def laSquare(a, nbits = 12, approx_until = 0):
    """Derivate of laMultiplication performing square operation"""

    return laMultiplication(a, a, nbits = nbits, approx_until=approx_until)

# In[36]:

# def laSqRoot(a, nbits = 16, approx_until = 0):
#     R = a
#     total_energy = 0

#     R_sq,enrg = laSquare(R, nbits, approx_until)
#     # print("R_sq:", R_sq)
#     total_energy += enrg

#     while (R_sq > a):
#         R, enrg = multiBitAdder(R, -1, nbits, approx_until)
#         # print("R:", R)
#         total_energy += enrg
#         R_sq,enrg = laSquare(R, nbits, approx_until)
#         # print("R_sq:", R_sq)
#         total_energy += enrg

#     return R,total_energy

def laSqRoot(a, nbits = 16, approx_until = 0):

    L = 0
    R,total_energy = multiBitAdder(a, 1, nbits, approx_until)
    R_min_one, enrg = multiBitAdder(R, -1, nbits, approx_until)
    total_energy += enrg

    while (L != R_min_one):
        R_plus_L, enrg = multiBitAdder(R, L, nbits, approx_until)
        M = R_plus_L >> 1
        total_energy += enrg
        M_sq,enrg = laSquare(M, nbits, approx_until)
        total_energy += enrg

        if (M_sq <= a):
            L = M
        else:
            R = M

        R_min_one, enrg = multiBitAdder(R, -1, nbits, approx_until)
        total_energy += enrg

    return L,total_energy
