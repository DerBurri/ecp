#!/usr/bin/env python3

# ## Using filters
#
# Some examples of using specified filters on our imported image.

from convolution import laConvolution

# Your code here
sample_image = io.imread("man.jpeg")
# print(sample_image.shape)

R_1 = sample_image[:, :, 0]
G_1 = sample_image[:, :, 1]
B_1 = sample_image[:, :, 2]

#formula for converting colour(RGB) to Gray Image scale Image
Y_sample = (0.299 * np.array(R_1)) + (0.587 * np.array(G_1)) + (0.114 * np.array(B_1))

# In[17]:

gauss_img, enrg = laConvolution(Y_sample.astype(int),gauss_filt.astype(int), nbits = 20, use_parallel=True)
print(enrg)
plt.imshow(gauss_img, cmap = "gray")


# In[18]:

gauss_img, enrg = laConvolution(Y_sample.astype(int),gauss_filt1.astype(int), nbits = 20, use_parallel=True)
print(enrg)
plt.imshow(gauss_img, cmap = "gray")


# In[19]:

horiz_edges, enrg = laConvolution(Y_sample.astype(int),sobel_horizontal.astype(int), use_parallel=True)
print(enrg)
plt.imshow(horiz_edges, cmap = "gray")


# In[20]:

vert_edges, enrg = laConvolution(Y_sample.astype(int),sobel_vertical.astype(int), use_parallel=True)
print(enrg)
plt.imshow(vert_edges, cmap = "gray")
