#!/usr/bin/env python3

import numpy as np
from scipy import signal

from convolution import laConvolution
from ecp_filters import gauss_filt1

def convol_test(matr, kernel, kernel_name = "undefined_name", nstages = 4, use_parallel = False, preprint_result = False, verbosity = 0):

    exact_convol = signal.convolve2d(matr, kernel, mode = "same")
    if preprint_result:
        print(exact_convol)

    appr_convol,enrg, prtime = laConvolution(np.array(matr),np.array(kernel), nstages, 0, use_parallel)

    par_string = "P" if use_parallel else ""

    if (not np.array_equal(exact_convol, appr_convol)):
        print("\033[91m", end='')
        print("Convolution{} with {} unsuccesful!".format(par_string,kernel_name))
        print("Exact convolution:")
        print(exact_convol.shape)
        print(exact_convol)
        print("My convolution:")
        print(appr_convol.shape)
        print(appr_convol)
        print("Energy:", enrg)
        print("Proc_time:", prtime)
        if verbosity > 0:
            print("Wrong elements:")
            diff_mask = appr_convol != exact_convol

            # Use np.where() to find the indices where the mask is True
            different_element_indices = np.where(diff_mask)

            # Print the positions of each different element
            for i, j in zip(*different_element_indices):
                print(f"Different element at position ({i}, {j}): {appr_convol[i, j]} (appr_convol) != {exact_convol[i, j]} (exact_convol)")

    else:
        print("\033[92m", end='')
        print("SUCCESS: Convolution{} with {}!".format(par_string, kernel_name))
        print("Energy:", enrg)
        print("Proc_time:", prtime)

    print("\033[0m", end='')

kern2 = [
    [0,1],
    [1,1]
]

kern3 = [
    [-1,2,1],
    [0,1,0],
    [1,2,-1]
]

kern4 = [
    [-1, 0, 1, 2],
    [ 0, 1, 2, 3],
    [ 1, 2, 3, 2],
    [ 2, 3, 2,-1]
]

kern5 = [
    [-1, 0, 1, 2, 2],
    [ 0, 1, 2, 3, 0],
    [ 1, 2, 3, 2, 9],
    [ 1, 2, 3, 2, 1],
    [ 2, 3, 2,-1,-3]
]

kern6 = [
    [-1, 0, 1, 2, 2, 2],
    [ 0, 1, 2, 3, 0, 3],
    [ 1, 2, 3, 2, 9, 2],
    [ 1, 2, 3, 2, 1, 2],
    [ 1, 2, 3, 2, 1, 2],
    [ 2, 3, 2,-1,-3,-1]
]

kern7 = [
    [-1, 0, 2, 1, 2, 2, 2],
    [ 0, 1, 3, 2, 3, 0, 3],
    [ 1, 2, 2, 3, 2, 9, 2],
    [ 1, 2, 2, 3, 2, 1, 2],
    [ 1, 2, 2, 3, 2, 1, 2],
    [ 1, 2, 2, 3, 2, 1, 2],
    [ 2, 3,-1, 2,-1,-3,-1]
]
random_matrix = [
    [12, 79, 27,  2, 45,  4, 41, 62],
    [ 0, 93,  4, 39, 24, 13, 76, 73],
    [35, 50, 36, 81,  3, 15, 50, 95],
    [80, 78, 61, 95,  5, 79, 12, 56],
    [95, 74, 65, 16, 89, 73, 13, 10],
    [51, 35, 34,  6, 25, 40,  3, 90],
    [84, 92, 32, 48, 17, 93,  5, 14],
    [52, 54, 32, 68, 79, 91, 68, 71]
]

# Tests:
convol_test(random_matrix, kern2, "kern2")
convol_test(random_matrix, kern3, "kern3")
convol_test(random_matrix, kern4, "kern4")
convol_test(random_matrix, gauss_filt1, "gauss_filt1", 16)
convol_test(random_matrix, kern2, "kern2", use_parallel=True)
convol_test(random_matrix, kern3, "kern3", use_parallel = True)
convol_test(random_matrix, kern4, "kern4", use_parallel = True)
convol_test(random_matrix, kern5, "kern5", nstages = 5, use_parallel = True)
convol_test(random_matrix, kern6, "kern6", nstages = 7, use_parallel = True)
convol_test(random_matrix, kern7, "kern7", nstages = 7, use_parallel = True)
convol_test(random_matrix, gauss_filt1, "gauss_filt1", nstages = 7, use_parallel = True)
array = np.random.randint(1, high = 50, size=(50,50))
convol_test(array, kern2, "kern2", use_parallel = True)
convol_test(array, kern3, "kern3", use_parallel = True)
convol_test(array, kern4, "kern4", use_parallel = True)
#convol_test(Y_sample.astype(int), kern4, "kern4", nstages = 5, use_parallel = False)
# convol_test(Y_sample.astype(int), kern4, "kern4", nstages = 5, use_parallel = True)
