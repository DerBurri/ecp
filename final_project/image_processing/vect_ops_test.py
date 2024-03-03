#!/usr/bin/env python3

import numpy as np
from itertools import permutations
from vect_ops import sumReduction, laAddVect, laMultiplicationVect, laSquareVect, laSqRootVect

np.random.seed(0)
for _ in range(10):
    array = np.random.randint(100, high = 1000, size=(5,5))
    res, enrg =  sumReduction(array, nbits = 16)
    print(f'sumReduction({array}) = {res, enrg}, correct: {res == np.sum(array)}')

# In[38]:

# Definition of test vectors and test permutations
test_matrices = np.array([
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]],

    [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]],

    [[2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]],

    [[18, 16, 14],
    [12, 10, 8],
    [6, 4, 2]]
])

test_vectors = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [3, 6, 9],
    [9, 6, 3]
])


test_matrix_permut = permutations(range(test_matrices.shape[0]), 2)

for i in test_matrix_permut:
    tst_matrix_a = test_matrices[i[0]]
    tst_matrix_b = test_matrices[i[1]]
    add_res, enrg = laAddVect(tst_matrix_a, tst_matrix_b)
    correct_res = tst_matrix_a + tst_matrix_b

    is_res_correct = np.array_equal(correct_res, add_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laAddVect of {tst_matrix_a} and {tst_matrix_b} = {add_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_matrix_permut = permutations(range(test_matrices.shape[0]), 2)

for i in test_matrix_permut:
    tst_matrix_a = test_matrices[i[0]]
    tst_matrix_b = test_matrices[i[1]]
    add_res, enrg = laAddVect(tst_matrix_a, tst_matrix_b, use_parallel= True)
    correct_res = tst_matrix_a + tst_matrix_b

    is_res_correct = np.array_equal(correct_res, add_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laAddVectP of {tst_matrix_a} and {tst_matrix_b} = {add_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_vector_permut = permutations(range(test_vectors.shape[0]), 2)

for i in test_vector_permut:
    tst_vector_a = test_vectors[i[0]]
    tst_vector_b = test_vectors[i[1]]
    add_res, enrg = laAddVect(tst_vector_a, tst_vector_b)
    correct_res = tst_vector_a + tst_vector_b

    is_res_correct = np.array_equal(correct_res, add_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laAddVect of {tst_vector_a} and {tst_vector_b} = {add_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_vector_permut = permutations(range(test_vectors.shape[0]), 2)

for i in test_vector_permut:
    tst_vector_a = test_vectors[i[0]]
    tst_vector_b = test_vectors[i[1]]
    add_res, enrg = laAddVect(tst_vector_a, tst_vector_b, use_parallel= True)
    correct_res = tst_vector_a + tst_vector_b

    is_res_correct = np.array_equal(correct_res, add_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laAddVectP of {tst_vector_a} and {tst_vector_b} = {add_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_matrix_permut = permutations(range(test_matrices.shape[0]), 2)

for i in test_matrix_permut:
    tst_matrix_a = test_matrices[i[0]]
    tst_matrix_b = test_matrices[i[1]]
    mult_res, enrg = laMultiplicationVect(tst_matrix_a,tst_matrix_b)
    correct_res = np.multiply(tst_matrix_a, tst_matrix_b)

    is_res_correct = np.array_equal(correct_res, mult_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laMultiplicationVect of {tst_matrix_a} and {tst_matrix_b} = {mult_res, enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_matrix_permut = permutations(range(test_matrices.shape[0]), 2)

for i in test_matrix_permut:
    tst_matrix_a = test_matrices[i[0]]
    tst_matrix_b = test_matrices[i[1]]
    mult_res, enrg = laMultiplicationVect(tst_matrix_a,tst_matrix_b, use_parallel = True)
    correct_res = np.multiply(tst_matrix_a, tst_matrix_b)

    is_res_correct = np.array_equal(correct_res, mult_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laMultiplicationVectP of {tst_matrix_a} and {tst_matrix_b} = {mult_res, enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_vector_permut = permutations(range(test_vectors.shape[0]), 2)

for i in test_vector_permut:
    tst_vector_a = test_vectors[i[0]]
    tst_vector_b = test_vectors[i[1]]
    mult_res, enrg = laMultiplicationVect(tst_vector_a, tst_vector_b)
    correct_res = np.multiply(tst_vector_a,tst_vector_b)

    is_res_correct = np.array_equal(correct_res, mult_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laMultiplicationVect of {tst_vector_a} and {tst_vector_b} = {mult_res, enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

test_vector_permut = permutations(range(test_vectors.shape[0]), 2)

for i in test_vector_permut:
    tst_vector_a = test_vectors[i[0]]
    tst_vector_b = test_vectors[i[1]]
    mult_res, enrg = laMultiplicationVect(tst_vector_a, tst_vector_b, use_parallel=True)
    correct_res = np.multiply(tst_vector_a,tst_vector_b)

    is_res_correct = np.array_equal(correct_res, mult_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laMultiplicationVectP of {tst_vector_a} and {tst_vector_b} = {mult_res, enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

for i in range(len(test_matrices)):
    square_res, enrg = laSquareVect(test_matrices[i])
    correct_res = np.multiply(test_matrices[i],test_matrices[i])
    is_res_correct = np.array_equal(correct_res, square_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSquareVect of {test_matrices[i]} = {square_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

for i in range(len(test_matrices)):
    square_res, enrg = laSquareVect(test_matrices[i], use_parallel=True)
    correct_res = np.multiply(test_matrices[i],test_matrices[i])
    is_res_correct = np.array_equal(correct_res, square_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSquareVectP of {test_matrices[i]} = {square_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

for i in range(len(test_vectors)):
    square_res, enrg = laSquareVect(test_vectors[i])
    correct_res = np.multiply(test_vectors[i],test_vectors[i])
    is_res_correct = np.array_equal(correct_res, square_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSquareVect of {test_vectors[i]} = {square_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

for i in range(len(test_vectors)):
    square_res, enrg = laSquareVect(test_vectors[i], use_parallel=True)
    correct_res = np.multiply(test_vectors[i],test_vectors[i])
    is_res_correct = np.array_equal(correct_res, square_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    print(f"laSquareVectP of {test_vectors[i]} = {square_res,enrg}, correct: {is_res_correct}")

    print("\033[0m", end='')

def test_sq_root_vect(array, nbits = 16, use_parallel = False):
    square_res, enrg = laSqRootVect(array, nbits, 0, use_parallel)
    correct_res = np.sqrt(array).astype(int)
    is_res_correct = np.array_equal(correct_res, square_res)

    if is_res_correct:
        print("\033[92m", end='')
    else:
        print("\033[91m", end='')

    par_p = "P" if use_parallel else ""

    print(f"laSqRootVect{par_p} of {array} = {square_res,enrg}, correct: {correct_res, is_res_correct}")

    print("\033[0m", end='')

for mtx in test_matrices:
    test_sq_root_vect(mtx, nbits = 16)

for mtx in test_matrices:
    test_sq_root_vect(mtx, nbits = 16, use_parallel = True)

for vect in test_vectors:
    test_sq_root_vect(vect, nbits = 16)

for vect in test_vectors:
    test_sq_root_vect(vect, nbits = 16, use_parallel = True)

np.random.seed(0)
array = np.random.randint(100, high = 1000, size=(5,5))
test_sq_root_vect(array, nbits = 20)
test_sq_root_vect(array, nbits = 20, use_parallel=True)
