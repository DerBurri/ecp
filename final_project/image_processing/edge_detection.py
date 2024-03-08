#!/usr/bin/env python
# coding: utf-8

# # Image processing 1: Edge detection using approximated adder
# 
# Author: Vladislav Válek

# In[29]:


# Loading required packages packages
import numpy as np
import matplotlib.pyplot as plt
import csv

from scipy import signal
from PIL import Image

from skimage import io, img_as_float, img_as_ubyte
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import peak_signal_noise_ratio as psnr
from math import ceil

from convolution import laConvolution
from ecp_filters import sobel_horizontal, sobel_vertical, gauss_filt1, gauss_filt
from vect_ops import laSquareVect, laSqRootVect, laAddVect

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
        print("INFO: stage_num_correction: Correcting number of stages: {} -> {}".format(nstages, new_nstages))

    return new_nstages

def normalize_image(image, newMin, newMax):
    image = (image - np.min(image)) * ((newMax - newMin) / (np.max(image) - np.min(image))) + newMin

    return image.astype(int)



# Function to perform convolution with the Sobel kernels
def sobelEdgeDetection(image, approx_until = 0, keep_nstages_constant = False):

    debug = True
    total_energy = 0
    total_prtime = 0
    nstages = 14

    if not keep_nstages_constant:
        peak_val = int(max(np.max(image), np.max(gauss_filt1)))
        nstages = stage_num_correction(peak_val, nstages)

    filt_img, enrg, prtime = laConvolution(image.astype(int), gauss_filt1, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("INFO: sobelEdgeDetection: Initial filtering done")
    total_energy += enrg
    total_prtime += prtime

    filt_img = normalize_image(filt_img, 0, 255)
    # print(np.max(filt_img))
    # print(np.min(filt_img))

    if not keep_nstages_constant:
        peak_val = int(max(np.max(filt_img), np.max(sobel_vertical), np.max(sobel_horizontal)))
        nstages = stage_num_correction(peak_val, nstages)

    # Apply convolution with the horizontal and vertical Sobel kernels
    h_edges, enrg, prtime = laConvolution(filt_img.astype(int), sobel_horizontal, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("INFO: sobelEdgeDetection: Horizontal convolution finished")
    total_energy += enrg
    total_prtime += prtime

    v_edges, enrg, prtime = laConvolution(filt_img.astype(int), sobel_vertical, nstages=nstages, approx_until=approx_until, use_parallel = True)
    print("INFO: sobelEdgeDetection: Vertical convolution finished")
    total_energy += enrg
    total_prtime += prtime

    if debug:
        print("DEBUG: sobelEdgeDetection: Detected maximum in h_edges: {}".format(np.max(h_edges)))
        print("DEBUG: sobelEdgeDetection: Detected minimum in h_edges: {}".format(np.min(h_edges)))
        print("DEBUG: sobelEdgeDetection: Detected maximum in v_edges: {}".format(np.max(v_edges)))
        print("DEBUG: sobelEdgeDetection: Detected minimum in v_edges: {}".format(np.min(v_edges)))

    h_edges = normalize_image(h_edges, -2**10, 2**10 -1)
    v_edges = normalize_image(v_edges, -2**10, 2**10 -1)

    if not keep_nstages_constant:
        peak_val = int(max(np.max(h_edges), np.max(v_edges)))
        nstages = stage_num_correction(peak_val, nstages)

    h_edg_sq, enrg, prtime = laSquareVect(h_edges.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("INFO: sobelEdgeDetection: Horizontal edge square finished")
    total_energy += enrg
    total_prtime += prtime

    v_edg_sq, enrg, prtime = laSquareVect(v_edges.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("INFO: sobelEdgeDetection: Vertical edge square finished")
    total_energy += enrg
    total_prtime += prtime

    if debug:
        print("DEBUG: sobelEdgeDetection: Detected maximum in h_edg_sq: {}".format(np.max(h_edg_sq)))
        print("DEBUG: sobelEdgeDetection: Detected minimum in h_edg_sq: {}".format(np.min(h_edg_sq)))
        print("DEBUG: sobelEdgeDetection: Detected maximum in v_edg_sq: {}".format(np.max(v_edg_sq)))
        print("DEBUG: sobelEdgeDetection: Detected minimum in v_edg_sq: {}".format(np.min(v_edg_sq)))

    h_edg_sq = normalize_image(h_edg_sq, 0, 2**20)
    v_edg_sq = normalize_image(v_edg_sq, 0, 2**20)

    # Calculate the magnitude of gradients
    magnitude_squared, enrg, prtime = laAddVect(h_edg_sq.astype(int), v_edg_sq.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    print("INFO: sobelEdgeDetection: Magnitude addition finished")
    total_energy += enrg
    total_prtime += prtime

    if debug:
        print("DEBUG: sobelEdgeDetection: Detected maximum in squared magnitude: {}".format(np.max(magnitude_squared)))
        print("DEBUG: sobelEdgeDetection: Detected minimum in squared magnitude: {}".format(np.min(magnitude_squared)))

    magnitude_squared = normalize_image(magnitude_squared, 0, 2**20)

    if not keep_nstages_constant:
        peak_val = int(np.max(magnitude_squared))
        nstages = stage_num_correction(peak_val, nstages)

    magnitude_approx, enrg, prtime = laSqRootVect(magnitude_squared.astype(int), nstages=nstages, approx_until=approx_until, use_parallel=True)
    total_energy += enrg
    total_prtime += prtime

    # Normalize the magnitude to the range [0, 255]
    magnitude_normalized = normalize_image(magnitude_approx, 0, 255)

    # Convert the magnitude to uint8 data type
    # magnitude_uint8 = magnitude_normalized.astype(np.uint8)
    magnitude_uint8 = magnitude_normalized

    return magnitude_uint8,total_energy, total_prtime, nstages

# det_edges, tot_energ = sobelEdgeDetection(Y_sample.astype(int))
# det_edges = sobelEdgeDetectionExact(Y_sample)
# print(det_edges)
# print(tot_energ)
# plt.imshow(det_edges, cmap = "gray")
# plt.show()

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

# ### Concluding analysis
# 
# This measures MSE, SSIM and PSNR when image processed by the LaConvolution function and by signal.convolve2d. The iteration over multiple approximation levels takes place as even more and more bits are approximated thus also the LaConvolution function's result gets more erroneous.

# In[1]:

def compare_image_operation(proc_tst, proc_exact):
    error = mse(proc_exact, proc_tst)
    print("INFO: compare_image_operation: MSE = {}".format(error))

    data_range = proc_exact.max() - proc_exact.min()

    similarity = ssim(proc_exact, proc_tst, data_range=data_range)
    print("INFO: compare_image_operation: SSIM = {}".format(similarity))
    peak_snr = psnr(proc_exact, proc_tst, data_range=data_range)
    print("INFO: compare_image_operation: PSNR = {}".format(peak_snr))

    return error, similarity, peak_snr

def approx_step_edge_detection(image, exact_edge_det, approx_until = 0):
    my_edge_det, energ, prtime, nstages = sobelEdgeDetection(image.astype(int), approx_until=approx_until, keep_nstages_constant = True)
    my_image = Image.fromarray(my_edge_det.astype(np.uint8), 'L')
    my_image.save('tst_edge_detect_{}.png'.format(approx_until))
    error, similarity, peak_snr = compare_image_operation(exact_edge_det, my_edge_det)
    print(f"INFO: approx_step_edge_detection: Captured test version with {approx_until} approximated stages")
    return error, similarity, peak_snr, energ, prtime, nstages

def approx_step_filtering(image, kern, kern_name, exact_image, approx_until = 0):
    filtered, enrg, prtime = laConvolution(image.astype(int), kern, nstages=14, approx_until=approx_until, use_parallel = True)
    filtered = normalize_image(filtered,0, 255)
    filtered_img = Image.fromarray(filtered.astype(np.uint8), 'L')
    filtered_img.save('tst_filtering_{}_{}.png'.format(approx_until, kern_name))
    error, similarity, peak_snr = compare_image_operation(exact_image, filtered)
    print(f"INFO: approx_step_filtering: Captured test version with {approx_until} approximated stages")
    return error, similarity, peak_snr, enrg, prtime


exact_edge_det = sobelEdgeDetectionExact(Y_sample)
exact_image = Image.fromarray(exact_edge_det.astype(np.uint8), 'L')
exact_image.save('ref_edge_detect.png')
# plt.imshow(exact_edge_det, cmap = "gray")
# plt.show()

table_rows = [['Op_type', 'Approx_level', 'MSE', 'SSIM', 'PSNR', 'Sum_energy', 'Sum_proctime']]

for appr_lvl in range(0, 8):
    error, similarity, peak_snr, energ, prtime,_ = approx_step_edge_detection(Y_sample, exact_edge_det, appr_lvl)
    table_rows.append(["EDGE", 0, error, similarity, peak_snr, energ, prtime])

# ===============================================================================
# Filtering with gauus filter of size 3x3
# ===============================================================================
exact_filtered =  signal.convolve2d(Y_sample, gauss_filt, mode = 'same')
exact_filtered = normalize_image(exact_filtered,0, 255)
exact_filtered_img = Image.fromarray(exact_filtered.astype(np.uint8), 'L')
exact_filtered_img.save('ref_filtered_3.png')

for appr_lvl in range(0, 8):
    error, similarity, peak_snr, energ, prtime = approx_step_filtering(Y_sample, gauss_filt, "gauss3", exact_filtered, appr_lvl)
    table_rows.append(["CONV_3", appr_lvl, error, similarity, peak_snr, energ, prtime])

# ===============================================================================
# Filtering with gauus filter of size 5x5
# ===============================================================================

exact_filtered =  signal.convolve2d(Y_sample, gauss_filt1, mode = 'same')
exact_filtered = normalize_image(exact_filtered,0, 255)
exact_filtered_img = Image.fromarray(exact_filtered.astype(np.uint8), 'L')
exact_filtered_img.save('ref_filtered_5.png')

for appr_lvl in range(0, 8):
    error, similarity, peak_snr, energ, prtime = approx_step_filtering(Y_sample, gauss_filt1, "gauss5", exact_filtered, appr_lvl)
    table_rows.append(["CONV_5", appr_lvl, error, similarity, peak_snr, energ, prtime])

print(table_rows)
with open('measured_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table_rows)
