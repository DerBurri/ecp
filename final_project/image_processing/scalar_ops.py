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

def laMultiplication(a, b, nstages = 12, approx_until = 0):
    """This accepts two parameters and performs artificial multiplication
    by successive addition."""

    # An identity value for multiplication is normally 1 but since this
    # multiplication is done by successive addition, the sum identity is taken
    # instead.
    res = 0
    total_energy = 0
    total_prtime = 0
    # a = a.astype(int)
    # b = a.astype(int)

    if (a == 0 or b == 0):
        return 0, 0, 0

    # Negative numbers have to be converted to the positive but the sign
    # has to remain for the result.
    neg_res_flag = True if ((a < 0 and b > 0) or (a > 0 and b < 0)) else False

    if a < 0:
        a, enrg, prtime = multiBitAdder(0,-a, nstages = nstages, approx_until = approx_until)
        total_energy += enrg
        total_prtime += prtime

    if b < 0:
        b, enrg, prtime = multiBitAdder(0,-b, nstages = nstages, approx_until = approx_until)
        total_energy += enrg
        total_prtime += prtime

    for _ in range(b):
        res, energy, prtime = multiBitAdder(res,a, nstages = nstages, approx_until = approx_until)
        total_energy += energy
        total_prtime += prtime

    if neg_res_flag:
        res *= -1

    return res, total_energy, total_prtime


def laSquare(a, nstages = 12, approx_until = 0):
    """Derivate of laMultiplication performing square operation"""

    return laMultiplication(a, a, nstages = nstages, approx_until=approx_until)

# In[36]:

# def laSqRoot(a, nstages = 16, approx_until = 0):
#     R = a
#     total_energy = 0

#     R_sq,enrg = laSquare(R, nstages, approx_until)
#     # print("R_sq:", R_sq)
#     total_energy += enrg

#     while (R_sq > a):
#         R, enrg = multiBitAdder(R, -1, nstages, approx_until)
#         # print("R:", R)
#         total_energy += enrg
#         R_sq,enrg = laSquare(R, nstages, approx_until)
#         # print("R_sq:", R_sq)
#         total_energy += enrg

#     return R,total_energy

# def laSqRoot(a, nstages = 16, approx_until = 0):

#     L = 0
#     R,total_energy, total_prtime = multiBitAdder(a, 1, nstages, approx_until)
#     R_min_one, enrg, prtime = multiBitAdder(R, -1, nstages, approx_until)
#     total_energy += enrg
#     total_prtime += prtime

#     while (L != R_min_one):
#         R_plus_L, enrg, prtime = multiBitAdder(R, L, nstages, approx_until)
#         M = R_plus_L >> 1
#         total_energy += enrg
#         total_prtime += prtime
#         M_sq,enrg, prtime = laSquare(M, nstages, approx_until)
#         total_energy += enrg
#         total_prtime += prtime

#         if (M_sq <= a):
#             L = M
#         else:
#             R = M

#         R_min_one, enrg, prtime = multiBitAdder(R, -1, nstages, approx_until)
#         total_energy += enrg
#         total_prtime += prtime

#     return L,total_energy, total_prtime

def laSqRoot(y, nstages = 16, approx_until = 0):

    L = 0
    a = 1
    d = 3

    total_energy = 0
    total_prtime = 0

    while (a <= y):
        na, enrg, prtime = multiBitAdder(a, d, nstages, approx_until)
        total_energy += enrg
        total_prtime += prtime
        nd, enrg, prtime = multiBitAdder(d, 2, nstages, approx_until)
        total_energy += enrg
        total_prtime += prtime
        nL , enrg, prtime = multiBitAdder(L, 1, nstages, approx_until)
        total_energy += enrg
        total_prtime += prtime

        if not ((na > a) and (nd > d) and (nL > L)):
            raise Exception("ERROR: laSqRoot: infinite loop inferred from unsufficient bit length of the adder")

        a = na
        d = nd
        L = nL

    return L, total_energy, total_prtime
