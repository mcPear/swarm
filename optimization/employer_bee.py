import random

from optimization.base_particle import BaseParticle


class EmployerBee(BaseParticle):
    def __init__(self, x):
        super().__init__(x)
        self.trials = 0

    def get_z(self, fun):
        if self.best_z is None:
            self.best_z = fun(self.x, self.y)
        return self.best_z
