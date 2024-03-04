#!/usr/bin/env python
# coding: utf-8

# # Image processing 1: Edge detection using approximated adder
# 
# Author: Vladislav Válek

# In[29]:


# Loading required packages packages
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

from skimage import io, img_as_float, img_as_ubyte
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import peak_signal_noise_ratio as psnr
from math import ceil

from convolution import laConvolution
from ecp_filters import sobel_horizontal, sobel_vertical, gauss_filt1, gauss_filt
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

# ## Sobel edge detection (exact)
#
# An exact version for reference

def sobelEdgeDetectionExact(image):
    image =  signal.convolve2d(image, gauss_filt1, mode = 'same')
    horizontal_edges = signal.convolve2d(image, sobel_horizontal, mode = 'same')
    vertical_edges = signal.convolve2d(image, sobel_vertical, mode = 'same')
    magnitude = np.sqrt(np.square(horizontal_edges) + np.square(vertical_edges))
    magnitude = ((magnitude - np.min(magnitude)) / (np.max(magnitude) - np.min(magnitude))) * 255
    # magnitude = magnitude.astype(np.uint8)
    return magnitude


# ## Sobel edge detection (approximate)
# 
# Uses all of the functions defined previously. The only thing not implemented is the division that is used
# to normalize an image. This is because the division on negative numbers is a very complicated operation. Other than
# that, all of the functions created using approximate addition.

# In[131]:

def stage_num_correction(peak_val, nstages):
    new_nstages = nstages
    bitlen = peak_val.bit_length()

    if (2*bitlen > nstages*3):
        new_nstages = int(ceil(2*bitlen / 3))
        print("Correcting number of stages: {} -> {}".format(nstages, new_nstages))

    return new_nstages


# Function to perform convolution with the Sobel kernels
def sobelEdgeDetection(image, approx_until = 0):

    total_energy = 0
    total_prtime = 0
    nstages = 4

    peak_val = int(max(np.max(image), np.max(gauss_filt1)))
    nstages = stage_num_correction(peak_val, nstages)

    filt_img, enrg, prtime = laConvolution(image.astype(int), gauss_filt1, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("Initial filtering done!")
    total_energy += enrg
    total_prtime += prtime

    filt_img = ((filt_img - np.min(filt_img)) / (np.max(filt_img) - np.min(filt_img))) * 255

    peak_val = int(max(np.max(filt_img), np.max(sobel_vertical), np.max(sobel_horizontal)))
    nstages = stage_num_correction(peak_val, nstages)

    # Apply convolution with the horizontal and vertical Sobel kernels
    h_edges, enrg, prtime = laConvolution(filt_img.astype(int), sobel_horizontal, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("Horizontal convolution finished!")
    total_energy += enrg
    total_prtime += prtime

    v_edges, enrg, prtime = laConvolution(filt_img.astype(int), sobel_vertical, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("Vertical convolution finished!")
    total_energy += enrg
    total_prtime += prtime

    # print(h_edges)
    # print(v_edges)

    peak_val = int(max(np.max(h_edges), np.max(v_edges)))
    nstages = stage_num_correction(peak_val, nstages)

    h_edg_sq, enrg, prtime = laSquareVect(h_edges.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("Horizontal edge square finished!")
    total_energy += enrg
    total_prtime += prtime

    v_edg_sq, enrg, prtime = laSquareVect(v_edges.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("Vertical edge square finished!")
    total_energy += enrg
    total_prtime += prtime

    # print(h_edg_sq)
    # print(v_edg_sq)

    # Calculate the magnitude of gradients
    magnitude_squared, enrg, prtime = laAddVect(h_edg_sq.astype(int), v_edg_sq.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("Magnitude addition finished!")
    total_energy += enrg
    total_prtime += prtime

    # print(np.max(magnitude_squared))
    # print(np.min(magnitude_squared))

    peak_val = int(np.max(magnitude_squared))
    nstages = stage_num_correction(peak_val, nstages)

    magnitude_approx, enrg, prtime = laSqRootVect(magnitude_squared.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    total_energy += enrg
    total_prtime += prtime

    # Normalize the magnitude to the range [0, 255]
    magnitude_normalized = ((magnitude_approx - np.min(magnitude_approx)) / (np.max(magnitude_approx) - np.min(magnitude_approx))) * 255

    # Convert the magnitude to uint8 data type
    # magnitude_uint8 = magnitude_normalized.astype(np.uint8)
    magnitude_uint8 = magnitude_normalized

    return magnitude_uint8,total_energy, total_prtime

# det_edges, tot_energ = sobelEdgeDetection(Y_sample.astype(int))
# det_edges = sobelEdgeDetectionExact(Y_sample)
# print(det_edges)
# print(tot_energ)
# plt.imshow(det_edges, cmap = "gray")
# plt.show()


# ### Concluding analysis
# 
# This measures MSE, SSIM and PSNR when image processed by the LaConvolution function and by signal.convolve2d. The iteration over multiple approximation levels takes place as even more and more bits are approximated thus also the LaConvolution function's result gets more erroneous.

# In[ ]:

def compare_image_operation(proc_tst, proc_exact):
    error = mse(proc_exact, proc_tst)
    print("    MSE = {}".format(error))

    data_range = proc_exact.max() - proc_exact.min()

    similarity = ssim(proc_exact, proc_tst, data_range=data_range)
    print("    SSIM = {}".format(similarity))
    peak_snr = psnr(proc_exact, proc_tst, data_range=data_range)
    print("    PSNR = {}".format(peak_snr))

exact_edge_det = sobelEdgeDetectionExact(Y_sample)
my_edge_det, energ, prtime = sobelEdgeDetection(Y_sample.astype(int))
print("Total energy: ", energ)
print("Total proctime: ", prtime)

compare_image_operation(exact_edge_det, my_edge_det)

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
