from tqdm import tqdm

from functions import matyas_func, rastrigin_func, levi_func
from optimization.abc import ABC
from optimization.eba import EBA
from optimization.pso import PSO
import matplotlib.pyplot as plt
import time

X_RESEARCH = 200


def now():
    return int(round(time.time() * 1000))


fun = matyas_func
iter_count = 10000
time_limit = 1000
plt.yscale('log')

x = X_RESEARCH
# --some-computation--
start = now()
pso = PSO(stop_func=lambda i: now() - start < time_limit)
pso_res = pso.optimize(fun, x)
# pso.optimize(x)

start = now()
abc = ABC(stop_func=lambda i: now() - start < time_limit)
abc_res = abc.optimize(fun, x)
# ba.optimize(x)

start = now()
eba = EBA(stop_func=lambda i: now() - start < time_limit)
eba_res = eba.optimize(fun, x)

print("PSO")
plt.plot(pso_res, label="PSO")
print("ABC")
plt.plot(abc_res, label="ABC")

print("EBA")
plt.plot(eba_res, label="EBA")
plt.legend()
plt.show()
# --end-of-some-computation--
