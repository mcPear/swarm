import random

from functions import rastrigin_func
from optimization.base_particle import BaseParticle
from optimization.optimizer import Optimizer


# r - pulse emission rate
# v - wave speed in air
# D - echolocation distance
# https://www.researchgate.net/publication/258478684_Bat_Algorithm_Inspired_Algorithm_for_Solving_Numerical_Optimization_Problems
class EBA(Optimizer):
    def __init__(self, animator=None, stop_func=lambda i: True):
        super().__init__(animator, stop_func)
        self.v = 0.17 * 5
        self.r = 0.5
        self.beta = lambda: random.uniform(0, 1)
        self.delta_T = lambda: random.uniform(-1, 1)
        self.D = lambda: self.v * self.delta_T() / 2

    def optimize(self, fun, start_pos_range, swarm_size=20):
        self.init(lambda: BaseParticle(start_pos_range), swarm_size, fun)
        results = []
        i = 0
        while self.stop_func(i):
            i += 1
            self.animate()
            for particle in self.swarm:
                # normal walk
                particle.x += self.D()
                particle.y += self.D()

                # # conditional random walk
                if random.random() > self.r:
                    particle.x = self.beta() * (self.optimum[0] - particle.x)
                    particle.y = self.beta() * (self.optimum[1] - particle.y)

                curr_z = fun(particle.x, particle.y)
                if curr_z < self.optimum[2]:
                    self.optimum = (particle.x, particle.y, curr_z)
                    print(curr_z)
            results.append(self.optimum[2])
        return results
