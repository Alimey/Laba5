from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def blur(img_array, weights_array, norm = True):
    """
    Вычисляет свертку изображения и нормированной весовой матрицы.
    """
    if norm:
        weights_array /= weights_array.sum()
    reds = np.asarray([np.zeros(len(img_array[0])) for i in range(len(img_array))])
    greens = np.asarray([np.zeros(len(img_array[0])) for i in range(len(img_array))])
    blues = np.asarray([np.zeros(len(img_array[0])) for i in range(len(img_array))])
    for i in range(len(img_array)):
        for k in range(len(img_array[0])):
            reds[i][k] = img_array[i][k][0]
            greens[i][k] = img_array[i][k][1]
            blues[i][k] = img_array[i][k][2]

    reds = ndimage.convolve(reds, weights_array)
    greens = ndimage.convolve(greens, weights_array)
    blues = ndimage.convolve(blues, weights_array)

    img_arr = img_array.copy()
    for i in range(len(img_arr)):
        for k in range(len(img_arr[0])):
            img_arr[i][k][0] = reds[i][k]
            img_arr[i][k][1] = greens[i][k]
            img_arr[i][k][2] = blues[i][k]

    return img_arr

# """Пример работы функции"""
# img = Image.open('бб.jpg').convert('RGB')
# img_arr = np.asarray(img)
# w = np.array([[1 for i in range(20)] for k in range(20)], dtype=float)
#
# ax1 = plt.subplot(121)
# ax2 = plt.subplot(122)
# ax1.imshow(img_arr)
# ax2.imshow(blur(img_arr, w))
# plt.show()
#
