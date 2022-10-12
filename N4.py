import math
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from DZ import N3


def gaussian_blur(img_array, sigma):
    """
    Выполняет гауссово размытие с заданной дисперсией
    """
    weights = np.zeros((2*round(sigma),2*round(sigma)))
    for i in range(2*round(sigma)):
        for k in range(2*round(sigma)):
            weights[i][k] = math.exp(-0.5*(1/math.pow(sigma,2)*(math.pow(1-k, 2) + math.pow(1-i, 2))))
    return N3.blur(img_array, weights)

# """Пример работы функции"""
# img = Image.open('бб.jpg').convert('RGB')
# img_arr = np.asarray(img)
#
# ax1 = plt.subplot(121)
# ax2 = plt.subplot(122)
# ax1.imshow(img_arr)
# ax2.imshow(gaussian_blur(img_arr, sigma=2.8))
# plt.show()
