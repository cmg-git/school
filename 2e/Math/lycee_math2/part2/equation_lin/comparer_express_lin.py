#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 08:34:00 2022

@author: cghiaus
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(start=-10, stop=10, step=0.1)

a1 = 2
b1 = 10
y1 = a1 * x + b1

a2 = -2
b2 = 10
y2 = a2 * x + b2

y_diff = y1 - y2

y1_label = f'$y_{1} = {a1} * x + {b1}$'
y2_label = f'$y_{2} = {a2} * x + {b2}$'
y_diff_label = 'y_diff'

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2)
ax.plot(x, y_diff, linestyle='--', color='red')
ax.set(xlabel='x',
       ylabel='y')
ax.legend([y1_label, y2_label, '$y_{diff}$'])
ax.grid()
plt.show()
