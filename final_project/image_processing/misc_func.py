#!/usr/bin/env python3

# # Operator skeletons
#
# Author: Vladislav Valek
#
# These are skeletons for vector operations used in this project. They also can decide if sequential
# of parallel version of the operator should be used.

import numpy as np

from multiprocessing import Pool, cpu_count

# In[37]:

def decideSeqPar(func, chunk_size, num_processes, inp_flat,  nbits = 12, approx_until = 0, use_parallel = False):
    if use_parallel:
        pool = Pool(processes=num_processes)  # Create a pool of processes

    chunk_indices = range(0, len(inp_flat[0]), chunk_size)

    if len(inp_flat) == 1:
        args = [(inp_flat[0][i:i+chunk_size], nbits, approx_until) for i in chunk_indices]
    elif len(inp_flat) == 2:
        args = [(inp_flat[0][i:i+chunk_size], inp_flat[1][i:i+chunk_size], nbits, approx_until) for i in chunk_indices]

    if use_parallel:
        results = pool.map(func, args)
    else:
        results =[[] for _ in range(len(args))]
        for i, arg in enumerate(args, 0):
            results[i] = func(arg)

    if use_parallel:
        pool.close()
        pool.join()
    return results

def binaryVectOp(func, a, b, nbits = 12, approx_until = 0, use_parallel = False):

    a_shap = a.shape

    if (a_shap != b.shape):
        return -1,-1

    a_flat = a.flat
    b_flat = b.flat

    res_flat = np.zeros_like(a_flat)
    total_energy = 0
    num_processes = min(cpu_count(), len(a_flat))
    chunk_size = int(np.ceil(len(a_flat) / num_processes))

    results = decideSeqPar(func, chunk_size, num_processes, (a_flat, b_flat), nbits, approx_until, use_parallel)
    for i, chunk_result in enumerate(results):
        for j, (r, energy) in enumerate(chunk_result):
            idx = i * chunk_size + j
            if idx < len(res_flat):
                res_flat[idx] = r
                total_energy += energy

    # Reshape the flattened result back to the original shape
    res = np.reshape(res_flat, a.shape)

    return res, total_energy

def unaryVectOp(func, a, nbits = 12, approx_until = 0, use_parallel = False):

    a_shap = a.shape
    a_flat = a.flat

    res_flat = np.zeros_like(a_flat)
    total_energy = 0
    num_processes = min(cpu_count(), len(a_flat))
    chunk_size = int(np.ceil(len(a_flat) / num_processes))

    results = decideSeqPar(func, chunk_size, num_processes, (a_flat,), nbits, approx_until, use_parallel)
    for i, chunk_result in enumerate(results):
        for j, (r, energy) in enumerate(chunk_result):
            idx = i * chunk_size + j
            if idx < len(res_flat):
                res_flat[idx] = r
                total_energy += energy

    # Reshape the flattened result back to the original shape
    res = np.reshape(res_flat, a.shape)

    return res, total_energy
