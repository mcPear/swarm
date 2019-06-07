from functions import rastrigin_func
from optimization.optimizer import Optimizer
from optimization.particle import Particle


class PSO(Optimizer):

    def __init__(self, animator, w=0.5):
        super().__init__(animator)
        self.wp = self.wg = self.w = w

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
    def optimize(self, start_pos_range, swarm_size=20, fun=rastrigin_func):
        self.init(lambda: Particle(start_pos_range), swarm_size, fun)
        while True:
            self.animator(self.swarm)
            for particle in self.swarm:
                particle.v_x = self.w * particle.v_x + self.wp * self.rand() * (particle.best_x - particle.x) + \
                               self.wg * self.rand() * (self.optimum[0] - particle.x)
                particle.v_y = self.w * particle.v_y + self.wp * self.rand() * (particle.best_y - particle.y) + \
                               self.wg * self.rand() * (self.optimum[1] - particle.y)

                particle.x += particle.v_x
                particle.y += particle.v_y

                curr_z = fun(particle.x, particle.y)
                if curr_z < particle.get_best_z(fun):
                    particle.best_x = particle.x
                    particle.best_y = particle.y
                    if curr_z < self.optimum[2]:
                        self.optimum = (particle.x, particle.y, curr_z)
                        print(curr_z)
