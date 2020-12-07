from PIL import Image

def cropImage(img, size):

    im = Image.open(img)

    if size is 'S':
        im_output_S = im.resize((32, 32))
        im_output_S.save('output_S.jpg')

    elif size is 'M':

        im_resize_M = im.resize((128, 128))

        im_crop_LU = im_resize_M.crop((0,0,64,64))
        im_crop_RU = im_resize_M.crop((64,0,128,64))
        im_crop_LD = im_resize_M.crop((0,64,64,128))
        im_crop_RD = im_resize_M.crop((64,64,128,128))

        im_crop_LU.save('output_M_1.jpg')
        im_crop_RU.save('output_M_2.jpg')
        im_crop_LD.save('output_M_3.jpg')
        im_crop_RD.save('output_M_4.jpg')

    elif size is 'L':

        im_resize = im.resize((360, 360))

        im_crop_UL = im_resize.crop((0, 0, 120, 120))
        im_crop_UM = im_resize.crop((120, 0, 240, 120))
        im_crop_UR = im_resize.crop((240, 0, 360, 120))
        im_crop_ML = im_resize.crop((0, 120, 120, 240))
        im_crop_MM = im_resize.crop((120, 120, 240, 240))
        im_crop_MR = im_resize.crop((240, 120, 360, 240))
        im_crop_DL = im_resize.crop((0, 240, 120, 360))
        im_crop_DM = im_resize.crop((120, 240, 240, 360))
        im_crop_DR = im_resize.crop((240, 240, 360, 360))

        im_crop_UL.save('output_L_1.jpg')
        im_crop_UM.save('output_L_2.jpg')
        im_crop_UR.save('output_L_3.jpg')
        im_crop_ML.save('output_L_4.jpg')
        im_crop_MM.save('output_L_5.jpg')
        im_crop_MR.save('output_L_6.jpg')
        im_crop_DL.save('output_L_7.jpg')
        im_crop_DM.save('output_L_8.jpg')
        im_crop_DR.save('output_L_9.jpg')

    else:
        return

import numpy as np
import skimage.measure
import torch

mat = np.arange(36).reshape(2,2,3,3)
print(mat)

# print(np.max(mat[0:2, 0:2]))

# a = []
# for i in range(0, 2):
#     for j in range(0, 2):
#
#         for k in range(0, 4, 1):
#             for l in range(0, 4, 1):
#                 a.append(np.max(mat[i][j][k:k + 1, l:l + 1]))
#                 print(np.max(mat[i][j][k:k + 1, l:l + 1]))

