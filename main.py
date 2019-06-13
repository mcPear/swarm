from animation import Animation
from functions import matyas_func, rastrigin_func, levi_func
from optimization.eba import EBA
from optimization.pso import PSO
from optimization.abc import ABC

X_RESEARCH = 20
X_ANIM = 5

x = X_RESEARCH
z = 100
fun = levi_func
anim = Animation()
anim.init(fun, x, z)

pso = PSO(anim.update)
# pso.optimize(fun, x)

abc = ABC(anim.update)
abc.optimize(fun, x, sources_count=50)

eba = EBA(anim.update)
# eba.optimize(fun, x)

anim.fix()
