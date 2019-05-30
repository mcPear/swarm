from animation import Animation
from functions import rastrigin_func
import time

anim = Animation()
anim.init(rastrigin_func)

# --some-computation--
anim.update([[1, 2], [0, 3]])
time.sleep(0.5)
anim.update([[0, 1], [1, 4]])
# --end-of-some-computation--

anim.fix()
