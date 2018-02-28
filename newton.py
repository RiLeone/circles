#!/usr/bin/env python3

"""
    Newton Circles
    ==============

    But not really.

    But in the end it should still be OK for running the code, right?

"""


import numpy as np
import matplotlib.pyplot as pltlib

class newtonCircles:
    def __init__(self, n = 20, growth_factor = .6):
        self._NOI = n
        self._figsize = (16, 9)
        self._gf = growth_factor
        self._r = 1.

    def draw_circle(self, center = None, radius = 1., axes = None):
        if center is None:
            center = [0., 0.]

        phi = 2 * np.pi * np.linspace(0, 1, 100)
        sphi = np.sin(phi)
        cphi = np.cos(phi)

        if axes == None:
            pltlib.plot(center[0] + radius * cphi, center[1] + radius * sphi, 'k', lw = 2)
        else:
            axes.plot(center[0] + radius * cphi, center[1] + radius * sphi, 'k', lw = 2)

    def draw_single_y(self):
        fig = pltlib.figure(figsize = self._figsize)
        ax = fig.add_subplot(111, aspect = 'equal')

        ax.axis('off')

        for ii in range(self._NOI):
            r = self._r * self._gf ** ii
            c = (0., r)
            self.draw_circle(c, r, ax)

        pltlib.savefig("plts/single_y.png")

    def draw_double_y(self):
        fig = pltlib.figure(figsize = self._figsize)
        ax = fig.add_subplot(111, aspect = 'equal')

        ax.axis('off')

        for ii in range(self._NOI):
            r = self._r * self._gf ** ii
            c_u = (0., r)
            c_d = (0., -r)
            self.draw_circle(c_u, r, ax)
            self.draw_circle(c_d, r, ax)

        pltlib.savefig("plts/double_y.png")

    def draw_m_outward(self, m = 2, save_frames = False):
        theta = 2 * np.pi / m

        fig = pltlib.figure(figsize = self._figsize)
        ax = fig.add_subplot(111, aspect = 'equal')

        r_lim = 2 * self._r + 2 * self._r / (1 - self._gf)
        ax.set_xlim((-r_lim, r_lim))
        ax.set_ylim((-r_lim, r_lim))
        ax.axis('off')

        self.draw_circle(radius = self._r / self._gf, axes = ax)
        if save_frames:
            pltlib.savefig("plts/frames/00000.png")

        cum_r = 0.

        for ii in range(self._NOI):
            r = self._r * self._gf ** ii

            for mm in range(m):
                c = ((2 * cum_r + r + self._r / self._gf) * np.cos(theta * mm), (2 * cum_r + r + self._r / self._gf) * np.sin(theta * mm))

                self.draw_circle(c, r, ax)
                if save_frames:
                    print("Savig outward frame {:d} of {:d}...".format(mm + ii * m + 1, m * self._NOI))
                    pltlib.savefig("plts/frames/{:05d}.png".format(mm + ii * m + 1))

            cum_r += r

        pltlib.savefig("plts/n{:d}_m{:d}_gf{:.1f}_outward.png".format(self._NOI, m, self._gf))

    def draw_m_inward(self, m = 2):
        theta = 2 * np.pi / m

        fig = pltlib.figure(figsize = self._figsize)
        ax = fig.add_subplot(111, aspect = 'equal')

        ax.axis('off')

        self.draw_circle(radius = self._r, axes = ax)

        for ii in range(1, self._NOI):
            r = self._r * self._gf ** ii
            c = (0., r)
            self.draw_circle(c, r, ax)

        pltlib.savefig("plts/m{:d}_inward.png".format(m))





if __name__ == "__main__":

    tester = newtonCircles()
    tester.draw_single_y()
    tester.draw_double_y()
    tester.draw_m_outward(m = 4, save_frames = True)

    pltlib.show()
