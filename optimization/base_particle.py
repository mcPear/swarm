import random


class BaseParticle:
    def __init__(self, x):
        self.x = random.randrange(-x, x)
        self.y = random.randrange(-x, x)
        self.best_z = None
