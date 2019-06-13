import numpy as np


def rastrigin_func(X, Y):
    Z = (X ** 2 - 10 * np.cos(2 * np.pi * X)) + \
        (Y ** 2 - 10 * np.cos(2 * np.pi * Y)) + 20
    return Z


def matyas_func(X, Y):
    Z = 0.26 * (X ** 2 + Y ** 2) + 0.48 * X * Y
    return Z


def levi_func(X, Y):
    Z = np.sin(3 * np.pi * X) ** 2 + (X - 1) ** 2 * (1 + np.sin(3 * np.pi * Y) ** 2) + (Y - 1) ** 2 * (
                1 + np.sin(2 * np.pi * Y) ** 2)
    return Z
