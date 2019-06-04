import random

from optimization.base_particle import BaseParticle


class Particle(BaseParticle):
    def __init__(self, x):
        super().__init__(x)
        self.best_x = self.x
        self.best_y = self.y
        self.v_x = random.randrange(-x, x)
        self.v_y = random.randrange(-x, x)

    def get_best_z(self, fun):
        if self.best_z is None:
            self.best_z = fun(self.best_x, self.best_y)
        return self.best_z
