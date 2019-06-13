from tqdm import tqdm

from functions import matyas_func, rastrigin_func, levi_func
from optimization.abc import ABC
from optimization.eba import EBA
from optimization.pso import PSO
from globals import X_RESEARCH, now, time_limit
import matplotlib.pyplot as plt
import numpy as np

fun = matyas_func
plt.yscale('log')

x = X_RESEARCH

res = []
for val in np.linspace(0, 1, 10, endpoint=True):
    semi_res = []
    for i in range(10):
        start = now()
        alg = ABC(stop_func=lambda i: now() - start < time_limit)
        best = alg.optimize(fun, x)[-1]
        semi_res.append(best)
    res.append(np.mean(semi_res))
plt.plot(res)
plt.show()
