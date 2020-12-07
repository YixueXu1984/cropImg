import numpy as np
import skimage.measure
import torch

w = np.arange(216).reshape(4,6,3,3)
print(w)


# def maxpooling2d(X, kernel_size):
#     N, C, size, _ = X.shape
#     out = []
#     out_size = (int)(size / kernel_size)
#     size_floor = (int)((np.floor(size / kernel_size)) * kernel_size)
#     print(size_floor)
#     a = []
#     print(size/kernel_size)
#
#     for i in range(0, N):
#         for j in range(0, C):
#
#             for k in range(0, size_floor, kernel_size):
#                 for l in range(0, size_floor, kernel_size):
#                     a.append(np.max(X[i][j][k:k + kernel_size, l:l + kernel_size]))
#     a = np.asarray(a)
#
#     out = a.reshape(N, C, out_size, out_size)
#     print(out)


