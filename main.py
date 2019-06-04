from animation import Animation
from functions import rastrigin_func
from optimization.eba import EBA
from optimization.pso import PSO
from optimization.abc import ABC

x = 20
z = 100
anim = Animation()
anim.init(rastrigin_func, x, z)

# --some-computation--
# pso = PSO(anim.update)
# pso.optimize(x)

ba = ABC(anim.update)
ba.optimize(x)
# --end-of-some-computation--

anim.fix()
