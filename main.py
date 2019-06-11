from animation import Animation
from functions import rastrigin_func
from optimization.eba import EBA
from optimization.pso import PSO
from optimization.abc import ABC

x = 5
z = 100
anim = Animation()
anim.init(rastrigin_func, x, z)

# --some-computation--
pso = PSO(anim.update)
# pso.optimize(x)

abc = ABC(anim.update)
abc.optimize(x)

eba = EBA(anim.update)
# eba.optimize(x)
# --end-of-some-computation--

anim.fix()
