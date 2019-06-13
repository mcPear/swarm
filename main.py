from animation import Animation
from functions import matyas_func, rastrigin_func, levi_func
from optimization.eba import EBA
from optimization.pso import PSO
from optimization.abc import ABC
from globals import X_ANIM

x = X_ANIM
z = 100
fun = levi_func
anim = Animation()
anim.init(fun, x, z)

pso = PSO(anim.update)
# pso.optimize(fun, x)

abc = ABC(anim.update)
abc.optimize(fun, x)

eba = EBA(anim.update)
# eba.optimize(fun, x)

anim.fix()
