import numpy as np
import random
from functions import rastrigin_func


class Particle:
    def __init__(self, x):
        self.x = random.randrange(-x, x)
        self.y = random.randrange(-x, x)
        self.best_x = self.x
        self.best_y = self.y
        self.best_z = None
        self.v_x = random.randrange(-2 * x, 2 * x)
        self.v_y = random.randrange(-2 * x, 2 * x)

    def get_best_z(self, evaluator):
        if self.best_z is None:
            self.best_z = evaluator(self.best_x, self.best_y)
        return self.best_z


def pso(animator, x, swarm_size=20, evaluator=rastrigin_func, w=0.5):
    optimum = (None, None, 999999)
    wp = wg = w
    rp = rg = random.random
    swarm = []

    for _ in range(swarm_size):
        particle = Particle(x)
        swarm.append(particle)
        z = evaluator(particle.x, particle.y)
        if z < optimum[2]:
            optimum = (particle.x, particle.y, z)

    # for each particle i = 1, ..., S do
    #    Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
    #    Initialize the particle's best known position to its initial position: pi ← xi
    #    if f(pi) < f(g) then
    #        update the swarm's best known  position: g ← pi
    #    Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)

    while True:
        animator(swarm)
        for particle in swarm:
            particle.v_x = w * particle.v_x + wp * rp() * (particle.best_x - particle.x) + \
                           wg * rg() * (optimum[0] - particle.x)
            particle.v_y = w * particle.v_y + wp * rp() * (particle.best_y - particle.y) + \
                           wg * rg() * (optimum[1] - particle.y)

            particle.x += particle.v_x
            particle.y += particle.v_y

            curr_z = evaluator(particle.x, particle.y)
            if curr_z < particle.get_best_z(evaluator):
                particle.best_x = particle.x
                particle.best_y = particle.y
                if curr_z < optimum[2]:
                    optimum = (particle.x, particle.y, curr_z)

    # while a termination criterion is not met do:
    #    for each particle i = 1, ..., S do
    #       for each dimension d = 1, ..., n do
    #          Pick random numbers: rp, rg ~ U(0,1)
    #          Update the particle's velocity: vi+1,d ← ω vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
    #       Update the particle's position: xi+1 ← xi + vi
    #       if f(xi) < f(pi) then
    #          Update the particle's best known position: pi ← xi
    #          if f(pi) < f(g) then
    #             Update the swarm's best known position: g ← pi
