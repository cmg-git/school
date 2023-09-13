#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:15:20 2022

@author: cghiaus
"""

import numpy as np
import matplotlib.pyplot as plt

i = np.array([0, 10, 20, 30, 40, 50, 60, 70])
r = np.array([0, 5, 13, 20, 26, 32, 37, 40])

fig, ax = plt.subplots()
ax.plot(r, i)
ax.set(xlabel='r',
       ylabel='i')
ax.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(np.sin(np.pi / 180 * r), np.sin(np.pi / 180 * i), '*')
ax.set(xlabel='sin(r)',
       ylabel='sin(i)')
ax.grid()
plt.show()
