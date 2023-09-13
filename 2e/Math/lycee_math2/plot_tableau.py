#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:14:14 2022

@author: cghiaus
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4, 5, 6],
        [-5, -4, 0, 4, 5, 7, 9], '-*')
ax.set_xlabel('x')
ax.set_ylabel('y = f(x)')
ax.grid()
plt.show()
