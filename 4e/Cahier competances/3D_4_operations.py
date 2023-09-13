#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:23:35 2021

@author: cghiaus
"""

import matplotlib.pyplot as plt
import numpy as np

# %matplotlib qt
plt.close('all')

# Make data.
rng = 5
no = 5 * 2 * rng + 1
rc, cc = 20, 20
x = np.linspace(-rng, rng, no)
y = x
X, Y = np.meshgrid(x, y)

xa, ya, za = np.zeros((3, 3))
u, v, w = np.array([[rng, 0, 0], [0, rng, 0], [0, 0, rng]])

# x + y
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X + Y, rcount=rc, ccount=cc, color='g')
ax.plot(x, np.zeros(np.size(y)), x, color='g', linewidth=5)
ax.plot(x, -y, 0, color='r', linewidth=5)
ax.plot(x, y, 2 * x, color='k', linewidth=5)

ax.quiver(xa, ya, za, u, v, w, arrow_length_ratio=0.1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x + y (red)')
plt.show()

# x - y
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X - Y, rcount=rc, ccount=cc, color='g')
ax.plot(x, np.zeros(np.size(y)), x, color='g', linewidth=5)
ax.plot(x, y, 0, color='r', linewidth=5)
ax.plot(x, -y, 2 * x, color='k', linewidth=5)

ax.quiver(xa, ya, za, u, v, w, arrow_length_ratio=0.1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x - y (black)')
plt.show()

# x * y
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X * Y, rcount=rc, ccount=cc, color='g')
ax.plot(x, np.ones(np.size(y)), x, color='g', linewidth=5)
ax.plot(x, np.zeros(np.size(y)), 0, color='r', linewidth=5)
ax.plot(np.zeros(np.size(x)), y, 0, color='r', linewidth=5)
ax.plot(x, x, x**2, color='k', linewidth=5)

ax.quiver(xa, ya, za, u, v, w, arrow_length_ratio=0.1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x * y (black)')
plt.show()


# x / y
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X, Y, X / Y, rcount=rc, ccount=cc, color='g')
ax.plot(x, np.ones(np.size(y)), x, color='g', linewidth=5)
ax.plot(np.zeros(np.size(x)), y, 0, color='r', linewidth=5)
ax.plot(x, x, 1, color='k', linewidth=5)

ax.quiver(xa, ya, za, u, v, w, arrow_length_ratio=0.1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('x * y (black)')
plt.show()
