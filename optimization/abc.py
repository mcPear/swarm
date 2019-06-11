import random
import copy

from functions import rastrigin_func
from optimization.employer_bee import EmployerBee
from optimization.base_particle import BaseParticle
from optimization.optimizer import Optimizer


# losowy init, tyle pracowników ile źródeł
# każda pracownica sprawdza somsiada
# zwiadowców podziel tak, żeby więcej poleciało tam, gdzie lepszy miód (info od pracownic, turniej)
# pracownica zmienia miejsce na losowe jeśli po 'trials' próbach sąsiedzi są ciągle gorsi

# a - greater 'a' means larger neighbourhood, works like learning rate
# trials - limit of iterations without finding new optimum for single bee
class ABC(Optimizer):
    def __init__(self, animator=None, a=3, trials=10, stop_func=lambda i: True):
        super().__init__(animator, stop_func)
        self.employers = []
        self.outlookers = []
        self.a = a
        self.trials = trials

    def optimize(self, start_pos_range, sources_count=20, fun=rastrigin_func):
        self.init_any_swarm(self.employers, lambda: EmployerBee(start_pos_range), sources_count, fun)
        self.init_any_swarm(self.outlookers, lambda: EmployerBee(start_pos_range), sources_count, fun)
        results = []
        iteration = 0
        while self.stop_func(iteration):
            iteration += 1
            self.animate()
            # send employers
            for i in range(len(self.employers)):
                self.employers[i] = self.find_better_neighbour_food_source(self.employers[i], start_pos_range, fun)
            # send outlookers
            for i in range(len(self.outlookers)):
                tournament_employers = random.sample(self.employers, sources_count // 4)
                tournament_winner = min(tournament_employers, key=lambda e: e.get_z(fun))
                self.outlookers[i].x = tournament_winner.x
                self.outlookers[i].y = tournament_winner.y
                self.outlookers[i].best_z = tournament_winner.best_z
                self.outlookers[i] = self.find_better_neighbour_food_source(self.outlookers[i], start_pos_range, fun)
                self.update_optimum(self.outlookers[i], fun)
            # send scouts
            for i in range(len(self.employers)):
                if self.employers[i].trials >= self.trials:
                    self.employers[i] = EmployerBee(start_pos_range)
                self.update_optimum(self.employers[i], fun)

            results.append(self.optimum[2])
        return results

    def find_better_neighbour_food_source(self, employer_bee, p, fun):
        x, y = employer_bee.x, employer_bee.y
        neighbour = EmployerBee(p)
        neighbour.x = x + self.fi(p) * (neighbour.x - x)
        neighbour.y = y + self.fi(p) * (neighbour.y - y)
        if neighbour.get_z(fun) < employer_bee.get_z(fun):
            return neighbour
        else:
            employer_bee.trials = employer_bee.trials + 1
            return employer_bee

    def fi(self, x):
        sign = -1 if self.rand() < 0.5 else 1
        # sign = 1
        return sign * self.rand() / x * self.a

    def update_optimum(self, bee, fun):
        z = bee.get_z(fun)
        if z < self.optimum[2]:
            self.optimum = (bee.x, bee.y, z)
            print(z)
