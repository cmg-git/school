#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:23:35 2021

@author: cghiaus
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# %matplotlib qt

# Make data.
no_range = 5
rc, cc = 20, 20
x = np.arange(-no_range, no_range + 1, 0.5)
y = np.arange(-no_range, no_range + 1, 0.5)
X, Y = np.meshgrid(x, y)
plt.close('all')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(X, Y, X * Y, rcount=rc, ccount=cc)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x * y')
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X - Y, rcount=rc, ccount=cc, color='k')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x - y')


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X - Y, rcount=rc, ccount=cc, color='k')
ax.plot_wireframe(X, Y, X + Y, rcount=rc, ccount=cc, color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x + y (black), x - y (red)')


# All three
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X * Y, rcount=rc, ccount=cc, color='b')
ax.plot_wireframe(X, Y, X - Y, rcount=rc, ccount=cc, color='k')
ax.plot_wireframe(X, Y, X + Y, rcount=rc, ccount=cc, color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('x*y (blue), x-y (black), x+y (red)')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, ((X * Y) > (X - Y)) * ((X - Y) > (X + Y)),
                  rcount=rc, ccount=cc, color='g')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('(x*y) > (x-y) > (x+y)')

plt.show()

# All three
X = np.arange(-no_range, 0 + 1)
Y = np.arange(-no_range, 0 + 1)
X, Y = np.meshgrid(X, Y)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X * Y, rcount=rc, ccount=cc, color='b')
ax.plot_wireframe(X, Y, X - Y, rcount=rc, ccount=cc, color='k')
ax.plot_wireframe(X, Y, X + Y, rcount=rc, ccount=cc, color='r')
ax.set_title('x*y (blue), x-y (black), x+y (red)')

v_min, v_max = -25, 25
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, X * Y, cmap=cm.coolwarm, vmin=v_min, vmax=v_max,
                       linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, X - Y, cmap=cm.coolwarm, vmin=v_min, vmax=v_max,
                       linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, X + Y, cmap=cm.coolwarm, vmin=v_min, vmax=v_max,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
