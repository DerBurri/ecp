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
    img_region, kernel, nbits, approx_until = args
    x, y = img_region.shape
    k, l = kernel.shape
    result = np.zeros((x - k + 1, y - l + 1))
    total_energy = 0

    for i in range(x - k + 1):
        for j in range(y - l + 1):
            region = img_region[i:i+k, j:j+l]
            reg_multiplicated, reg_mult_enrg = laMultiplicationVect(region, kernel, nbits = nbits, approx_until=approx_until)
            total_energy += reg_mult_enrg
            result[i, j], energy = sumReduction(reg_multiplicated, nbits = nbits, approx_until=approx_until)
            #result[i, j], energy = sumReduction(region * kernel, nbits = nbits, approx_until=approx_until)
            total_energy += energy
            #result[i, j] = np.sum(region * kernel)

    return result, total_energy

def conv_par(image, kernel, nbits = 12, approx_until = 0):
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2 - (1 if k % 2 == 0 else 0)),(l // 2, l // 2 - (1 if k % 2 == 0 else 0))), mode = "constant")
    xp, _ = pad_image.shape
    flipped_kernel = np.flipud(np.fliplr(kernel))
    num_processes = min(cpu_count(), xp // k)
    total_energy = 0

    overlap_width = round(k / 2)

    chunk_size = (xp + num_processes - 1) // num_processes

    chunks = [(pad_image[0:k, : ], flipped_kernel, nbits, approx_until)]

    for i in range(k, xp, chunk_size):
        end_row = min(i + chunk_size, xp)
        image_chunk = pad_image[i - (k-1):end_row, :]
        chunks.append((image_chunk, flipped_kernel, nbits, approx_until))

    # # Parallel processing
    with Pool(processes=num_processes) as pool:
        results = pool.map(convolve_region, chunks)

    # Combine results
    result, total_energy = zip(*results)
    combined_result = np.concatenate(result, axis = 0).astype(int)

    total_energy = sum(total_energy)

    return combined_result, total_energy


def conv_seq(image, kernel, nbits = 12, approx_until = 0):
    x, y           = image.shape
    k, l           = kernel.shape
    pad_image      = np.pad(image, ((k // 2, k // 2),(l // 2, l // 2)), mode = "constant")
    result         = np.zeros_like(image)
    flipped_kernel = np.flipud(np.fliplr(kernel))
    total_energy   = 0

    for i in range(x):
        for j in range(y):
            region = pad_image[i:i + k, j:j + l]
            reg_multiplicated, reg_mult_enrg = laMultiplicationVect(region, flipped_kernel, nbits = nbits, approx_until=approx_until)
            total_energy += reg_mult_enrg
            result[i, j], energy = sumReduction(reg_multiplicated, nbits = nbits, approx_until=approx_until)
            total_energy += energy

    return result, energy

def laConvolution(image, kernel, nbits = 12, approx_until = 0, use_parallel = True):
    if use_parallel:
        return conv_par(image, kernel, nbits, approx_until)
    else:
        return conv_seq(image, kernel, nbits, approx_until)
