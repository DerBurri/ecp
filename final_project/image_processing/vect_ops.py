#!/usr/bin/env python3

# ### Vector functions
#
# Author: Vladislav Valek
#
# These can be applied either on matrices or vectors.

import numpy as np

from adder_definitions import multiBitAdder
from scalar_ops import laMultiplication, laSqRoot, laSquare
from misc_func import binaryVectOp, unaryVectOp

# In[34]:

def sumReduction(n, nstages = 12, approx_until = 0):

    # n = n.astype(int)
    shap = n.shape
    total_energy = 0
    total_prtime = 0

    if (len(shap) == 1):
        res = n[0]

        for i in range(1,shap[0]):
            res,energy,prtime = multiBitAdder(res,n[i], nstages = nstages, approx_until = approx_until)
            total_energy += energy
            total_prtime += prtime

    elif (len(shap) == 2):
        res = n[0,0]

        for i in range(shap[0]):
            for j in range(shap[1]):

                # There is no reason to calculating this because we are reducing a matrix so
                # first element is only saved and the algorithm goes on.
                if (i == 0 and j == 0): continue

                res,energy,prtime = multiBitAdder(res,n[i,j], nstages = nstages, approx_until = approx_until)
                total_energy += energy
                total_prtime += prtime

    return res, total_energy, total_prtime

# In[53]:

def add_chunk(args):
    a_chunk, b_chunk, nstages, approx_until = args
    return [multiBitAdder(a_elem, b_elem, nstages, approx_until) for a_elem, b_elem in zip(a_chunk, b_chunk)]

def laAddVect(a, b, nstages = 12, approx_until = 0, use_parallel = False):
    return binaryVectOp(add_chunk, a, b, nstages, approx_until, use_parallel)

# In[52]:

def multiply_chunk(args):
    a_chunk, b_chunk, nstages, approx_until = args
    return [laMultiplication(a_elem, b_elem, nstages, approx_until) for a_elem, b_elem in zip(a_chunk, b_chunk)]

def laMultiplicationVect(a, b , nstages = 12, approx_until = 0, use_parallel = False):
    return binaryVectOp(multiply_chunk, a, b, nstages, approx_until, use_parallel)

# In[50]:

def square_chunk(args):
    a_chunk, nstages, approx_until = args
    return [laSquare(a_elem, nstages, approx_until) for a_elem in a_chunk]

def laSquareVect(a, nstages = 12, approx_until = 0, use_parallel = False):
    return unaryVectOp(square_chunk, a, nstages, approx_until, use_parallel)

# In[45]:

def root_square_chunk(args):
    a_chunk, nstages, approx_until = args
    return [laSqRoot(a_elem, nstages, approx_until) for a_elem in a_chunk]

def laSqRootVect(a, nstages = 12, approx_until = 0, use_parallel = False):
    return unaryVectOp(root_square_chunk, a, nstages, approx_until, use_parallel)
