import random

from functions import rastrigin_func
from optimization.base_particle import BaseParticle
from optimization.optimizer import Optimizer


# r - pulse emission rate
# v - wave speed in air
# D - echolocation distance
# https://www.researchgate.net/publication/258478684_Bat_Algorithm_Inspired_Algorithm_for_Solving_Numerical_Optimization_Problems
class EBA(Optimizer):
    def __init__(self, animator):
        super().__init__(animator)
        self.v = 0.17
        self.r = 0.5
        self.beta = lambda: random.uniform(0, 1)
        self.delta_T = lambda: random.uniform(-1, 1)
        self.D = lambda: self.v * self.delta_T() / 2

    def optimize(self, start_pos_range, swarm_size=20, fun=rastrigin_func):
        self.init(lambda: BaseParticle(start_pos_range), swarm_size, fun)
        while True:
            self.animator(self.swarm)
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
