#!/usr/bin/env python3

# ## Function "LaConvolution"
#
# Author: Vladislav Valek
#
# This function performs a standard convolution on an image the same way as signal.convolve2d with mode set to 'same'. This outputs the resulting image with the same size as the input image.

import numpy as np
from multiprocessing import Pool, cpu_count

from vect_ops import laMultiplicationVect, sumReduction

# In[16]:

def convolve_region(args):
    img_region, kernel, nstages, approx_until = args
    x, y = img_region.shape
    k, l = kernel.shape
    result = np.zeros((x - k + 1, y - l + 1))
    total_energy = 0
    total_prtime = 0

    for i in range(x - k + 1):
        for j in range(y - l + 1):
            region = img_region[i:i+k, j:j+l]
            reg_multiplicated, reg_mult_enrg,prtime = laMultiplicationVect(region, kernel, nstages = nstages, approx_until=approx_until)
            total_energy += reg_mult_enrg
            total_prtime += prtime
            result[i, j], energy, prtime = sumReduction(reg_multiplicated, nstages = nstages, approx_until=approx_until)
            #result[i, j], energy = sumReduction(region * kernel, nstages = nstages, approx_until=approx_until)
            total_energy += energy
            total_prtime += prtime
            #result[i, j] = np.sum(region * kernel)

    return result, total_energy, total_prtime

def conv_par(image, kernel, nstages = 4, approx_until = 0):
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2 - (1 if k % 2 == 0 else 0)),(l // 2, l // 2 - (1 if k % 2 == 0 else 0))), mode = "constant")
    xp, _ = pad_image.shape
    flipped_kernel = np.flipud(np.fliplr(kernel))
    num_processes = min(cpu_count(), xp // k)
    total_energy = 0
    total_prtime = 0

    overlap_width = round(k / 2)

    chunk_size = (xp + num_processes - 1) // num_processes

    chunks = [(pad_image[0:k, : ], flipped_kernel, nstages, approx_until)]

    for i in range(k, xp, chunk_size):
        end_row = min(i + chunk_size, xp)
        image_chunk = pad_image[i - (k-1):end_row, :]
        chunks.append((image_chunk, flipped_kernel, nstages, approx_until))

    # # Parallel processing
    with Pool(processes=num_processes) as pool:
        results = pool.map(convolve_region, chunks)

    # Combine results
    result, total_energy, total_prtime = zip(*results)
    combined_result = np.concatenate(result, axis = 0).astype(int)

    total_energy = sum(total_energy)
    total_prtime = sum(total_prtime)

    return combined_result, total_energy, total_prtime


def conv_seq(image, kernel, nstages = 4, approx_until = 0):
    x, y           = image.shape
    k, l           = kernel.shape
    pad_image      = np.pad(image, ((k // 2, k // 2),(l // 2, l // 2)), mode = "constant")
    result         = np.zeros_like(image)
    flipped_kernel = np.flipud(np.fliplr(kernel))
    total_energy   = 0
    total_prtime   = 0

    for i in range(x):
        for j in range(y):
            region = pad_image[i:i + k, j:j + l]
            reg_multiplicated, reg_mult_enrg, prtime = laMultiplicationVect(region, flipped_kernel, nstages = nstages, approx_until=approx_until)
            total_energy += reg_mult_enrg
            total_prtime += prtime
            result[i, j], energy, prtime = sumReduction(reg_multiplicated, nstages = nstages, approx_until=approx_until)
            total_energy += energy
            total_prtime += prtime

    return result, total_energy, total_prtime

def laConvolution(image, kernel, nstages = 4, approx_until = 0, use_parallel = True):
    if use_parallel:
        return conv_par(image, kernel, nstages, approx_until)
    else:
        return conv_seq(image, kernel, nstages, approx_until)
