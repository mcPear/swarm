import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class Animation:

    def init(self, optim_func):
        X = np.linspace(-6, 6, 100)
        Y = np.linspace(-6, 6, 100)
        X, Y = np.meshgrid(X, Y)
        Z = optim_func(X, Y)
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')
        self.ax.view_init(80, 30)
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.nipy_spectral, linewidth=0.08, antialiased=True)
        plt.pause(0.001)
        self.lines = []
        self.out_of_date = False
        self.fig.canvas.mpl_connect('close_event', self.handle_close)

    def update(self, swarm):

        for line in self.lines:
            l = line.pop(0)
            l.remove()
            del l

        for warm in swarm:
            x, y = warm
            x = [x, x]
            y = [y, y]
            z = [0, 100]
            line = self.ax.plot(x, y, z, 'k-', alpha=1, linewidth=1.5)
            self.lines.append(line)
        self.fig.canvas.draw()
        plt.pause(0.001)

    def fix(self):
        plt.pause(0)

    def handle_close(self, evt):
        exit(0)
