#!/usr/bin/env python
# coding: utf-8

# # Image processing 1: Edge detection using approximated adder
# 
# Author: Vladislav Válek

# In[29]:


# Loading required packages packages
import numpy as np
import matplotlib.pyplot as plt

from skimage import io, img_as_float, img_as_ubyte
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import peak_signal_noise_ratio as psnr

from convolution import laConvolution
from ecp_filters import sobel_horizontal, sobel_vertical
from vect_ops import laSquareVect, laSqRootVect, laAddVect

# ## Import sample image
# 
# A sample image is a very sympathetic man that uses its old camera to take photos.

# In[15]:

# Your code here
sample_image = io.imread("man.jpeg")
# print(sample_image.shape)

R_1 = sample_image[:, :, 0] 
G_1 = sample_image[:, :, 1]
B_1 = sample_image[:, :, 2]

#formula for converting colour(RGB) to Gray Image scale Image
Y_sample = (0.299 * np.array(R_1)) + (0.587 * np.array(G_1)) + (0.114 * np.array(B_1)) 

# plt.imshow(Y_sample , cmap = "gray")
# print(Y_sample.shape)
# print(Y_sample)


# ## Sobel edge detection
# 
# This uses two filters specified previously.

# In[131]:

# Function to perform convolution with the Sobel kernels
def sobelEdgeDetection(image, nbits = 12, approx_until = 0):

    total_energy = 0

    # filt_img= signal.convolve2d(image, f1, mode = "same")

    # Apply convolution with the horizontal and vertical Sobel kernels
    h_edges, h_enrg = laConvolution(image.astype(int), sobel_horizontal, nbits=nbits, approx_until=approx_until, use_parallel = True)
    print("Horizontal convolution finished!")
    total_energy += h_enrg
    v_edges, v_enrg = laConvolution(image.astype(int), sobel_vertical, nbits=nbits, approx_until=approx_until, use_parallel = True)
    print("Vertical convolution finished!")
    total_energy += v_enrg

    print(h_edges)
    print(v_edges)

    nbits = 32

    h_edg_sq, h_edg_sq_eng= laSquareVect(h_edges.astype(int), nbits=nbits, approx_until=approx_until, use_parallel=True)
    print("Horizontal edge square finished!")
    total_energy += h_edg_sq_eng 
    v_edg_sq, v_edg_sq_eng= laSquareVect(v_edges.astype(int), nbits=nbits, approx_until=approx_until, use_parallel=True)
    print("Vertical edge square finished!")
    total_energy += v_edg_sq_eng 

    print(h_edg_sq)
    print(v_edg_sq)

    # Calculate the magnitude of gradients
    magnitude_squared, mag_sq_eng = laAddVect(h_edg_sq.astype(int), v_edg_sq.astype(int), nbits=nbits, approx_until=approx_until, use_parallel=True) 
    print("Magnitude addition finished!")
    total_energy += mag_sq_eng 

    # magnitude_approx = np.sqrt(magnitude_squared.astype(int))
    magnitude_approx, mag_appr_eng = laSqRootVect(magnitude_squared.astype(int), nbits=nbits, approx_until=approx_until, use_parallel=True)
    total_energy += mag_appr_eng

    # Normalize the magnitude to the range [0, 255]
    # print(np.max(magnitude_approx))
    magnitude_normalized = ((magnitude_approx - np.min(magnitude_approx)) / (np.max(magnitude_approx) - np.min(magnitude_approx))) * 255

    # Convert the magnitude to uint8 data type
    # magnitude_uint8 = magnitude_normalized.astype(np.uint8)
    magnitude_uint8 = magnitude_normalized

    return magnitude_uint8,total_energy

det_edges, tot_energ = sobelEdgeDetection(Y_sample.astype(int), nbits = 25)
print(det_edges)
print(tot_energ)
# plt.imshow(det_edges, cmap = "gray")


# ### Concluding analysis
# 
# This measures MSE, SSIM and PSNR when image processed by the LaConvolution function and by signal.convolve2d. The iteration over multiple approximation levels takes place as even more and more bits are approximated thus also the LaConvolution function's result gets more erroneous.

# In[ ]:


# exact_convolution_result = signal.convolve2d(Y_sample, sobel_horizontal, mode = "same")

# # Your code here
# for i in range(8):
#     print("Number of approximated bits on addition: ", i)
#     approx_convolution_result,_ = laConvolution(Y_sample, sobel_horizontal, i)

#     data_range = exact_convolution_result.max() - exact_convolution_result.min()

#     # Compare results and calculate error/similarity
#     error = mse(exact_convolution_result, approx_convolution_result)
#     print("    MSE = {}".format(error))
#     similarity = ssim(exact_convolution_result, approx_convolution_result, data_range=data_range)
#     print("    SSIM = {}".format(similarity))
#     peak_snr = psnr(exact_convolution_result, approx_convolution_result, data_range=data_range)
#     print("    PSNR = {}".format(peak_snr))
