import random


class Optimizer:

    def __init__(self, animator, stop_func):
        super().__init__()
        self.optimum = (None, None, 999999)
        # TODO check if rand from [0,1] is ok, was [0, 1)
        self.rand = lambda: random.uniform(0, 1)
        self.swarm = []
        self.animator = animator
        self.stop_func = stop_func

    # for each particle i = 1, ..., S do
    #    Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
    #    Initialize the particle's best known position to its initial position: pi ← xi
    #    if f(pi) < f(g) then
    #        update the swarm's best known  position: g ← pi
    #    Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)
    def init(self, particle_constructor, swarm_size, fun):
        self.init_any_swarm(self.swarm, particle_constructor, swarm_size, fun)

    def init_any_swarm(self, swarm, particle_constructor, swarm_size, fun):
        for _ in range(swarm_size):
            particle = particle_constructor()
            swarm.append(particle)
            z = fun(particle.x, particle.y)
            if z < self.optimum[2]:
                self.optimum = (particle.x, particle.y, z)

    def animate(self):
        if self.animator is not None:
            self.animator(self.swarm)
