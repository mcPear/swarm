from tqdm import tqdm

from functions import matyas_func, rastrigin_func, levi_func
from optimization.abc import ABC
from optimization.eba import EBA
from optimization.pso import PSO
from globals import X_RESEARCH, now, time_limit
import matplotlib.pyplot as plt


fun = matyas_func
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
