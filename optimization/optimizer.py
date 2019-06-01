import random


class Optimizer:

    def __init__(self, animator):
        super().__init__()
        self.optimum = (None, None, 999999)
        # TODO check if rand from [0,1] is ok, was [0, 1)
        self.rp = self.rg = lambda: random.uniform(0, 1)
        self.swarm = []
        self.animator = animator

    # for each particle i = 1, ..., S do
    #    Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
    #    Initialize the particle's best known position to its initial position: pi ← xi
    #    if f(pi) < f(g) then
    #        update the swarm's best known  position: g ← pi
    #    Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)
    def init(self, particle_constructor, swarm_size, fun):
        for _ in range(swarm_size):
            particle = particle_constructor()
            self.swarm.append(particle)
            z = fun(particle.x, particle.y)
            if z < self.optimum[2]:
                self.optimum = (particle.x, particle.y, z)
