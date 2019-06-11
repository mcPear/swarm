from tqdm import tqdm

from functions import rastrigin_func
from optimization.abc import ABC
from optimization.eba import EBA
from optimization.pso import PSO
import matplotlib.pyplot as plt

iter_count = 10000
plt.yscale('log')

x = 5
z = 100
# --some-computation--
pso = PSO(stop_func=lambda i: i < iter_count)
pso_res = pso.optimize(x)
# pso.optimize(x)

abc = ABC(stop_func=lambda i: i < iter_count)
abc_res = abc.optimize(x)
# ba.optimize(x)

eba = EBA(stop_func=lambda i: i < iter_count)
eba_res = eba.optimize(x)

print("PSO")
plt.plot(pso_res, label="PSO")
print("ABC")
plt.plot(abc_res, label="ABC")

print("EBA")
plt.plot(eba_res, label="EBA")
plt.legend()
plt.show()
# --end-of-some-computation--
