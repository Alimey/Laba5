import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(x_low, x_high, y_low, y_high, points_x, points_y):
    """
    Создает изображение множества Мандельброта в диапазоне по x от x_low до x_high,
    по y - от y_low до y_high с разрешением points_x*points_y
    """
    infinity = 10
    max_iterations = 10
    # x, y - действительная и мнимая части
    x = np.linspace(x_low, x_high, points_x)
    y = np.linspace(y_low, y_high, points_y)
    # Будущая картинка
    img = np.zeros((points_x, points_y))
    # Перебираем точки комплексной плоскости
    for ind_a, a in enumerate(x):
        for ind_b, b in enumerate(y):

            z = 0
            c = a + 1j * b
            # Проводим 10 итераций и смотрим на значение комплексного числа
            for i in range(max_iterations):
                z = z**2 + c
                if np.abs(z)>=infinity:
                    img[ind_a][ind_b] -= 1


    return img

plt.yticks([])
plt.xticks([])
plt.imshow(mandelbrot(-2.5, 1.5, -2, 2, 300, 300).T, cmap='Greys')
plt.show()
