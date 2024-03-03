#!/usr/bin/env python
# coding: utf-8
#
# # ECP Filters: file containing used filters in the project
#
# Author: Vladislav Valek

# ## Filters for image processing
#
# 1) Low Pass Filter
#
#     - f1: Low pass average filter
#     - gauss_filt : Low pass to remove noise from image
#     - gauss_filt1 : same as before but bigger
#
#     These filters are designed for tasks such as removing noise from images or smoothing/blurring images. The key characteristic is that the sum of all the kernel elements should be one.
#
# 2) Filters for edge detection
#
#     - sobel_vertical   : Sobel vertical edge filter
#     - sobel_horizontal : Sobel horizontal edge filter
#
#     These filters are a form of high-pass filters. The sum of all elements within each of them should be 0.

# In[1]:

import numpy as np

f1 = [
    [ 1, -1,  1],
    [-1,  1, -1],
    [ 1, -1,  1]
]
f1 = np.array(f1)

gauss_filt = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

gauss_filt1 = np.array([
    [1, 4,  7,  4,  1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4,  7,  4,  1]
])

sobel_vertical = [
    [ 1,  2,  1],
    [ 0,  0,  0],
    [-1, -2, -1]
]
sobel_vertical = np.array(sobel_vertical)

sobel_horizontal = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]
sobel_horizontal = np.array(sobel_horizontal)
