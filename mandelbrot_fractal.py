import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Вычисление количества итераций для точки в множестве Мандельброта.

    Parameters:
    c (complex): Комплексное число.
    max_iter (int): Максимальное количество итераций.

    Returns:
    int: Количество итераций.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Создание изображения множества Мандельброта.

    Parameters:
    width (int): Ширина изображения.
    height (int): Высота изображения.
    x_min (float): Минимальное значение по оси x.
    x_max (float): Максимальное значение по оси x.
    y_min (float): Минимальное значение по оси y.
    y_max (float): Максимальное значение по оси y.
    max_iter (int): Максимальное количество итераций.

    Returns:
    np.ndarray: Массив значений итераций.
    """
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color
    return image

def plot_mandelbrot(image, cmap='inferno'):
    """
    Визуализация множества Мандельброта.

    Parameters:
    image (np.ndarray): Массив значений итераций.
    cmap (str): Цветовая карта.

    Returns:
    None
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap=cmap, extent=(-2, 1, -1.5, 1.5))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

if __name__ == "__main__":
    width = 800
    height = 800
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 1000

    mandelbrot_image = create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot(mandelbrot_image)
