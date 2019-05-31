from animation import Animation
from functions import rastrigin_func
import time
from pso import pso

x = 20
z = 100
anim = Animation()
anim.init(rastrigin_func, x, z)

# --some-computation--
pso(anim.update, x)
# --end-of-some-computation--

anim.fix()
