#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 08:34:00 2022

@author: cghiaus
"""

import numpy as np
import matplotlib.pyplot as plt


def comparison_1degree(x, param1, param2):
    a1, b1 = param1
    a2, b2 = param2
    y2 = a2 * x + b2
    y1 = a1 * x + b1

    y_diff = y1 - y2
    if a1 - a2 != 0:
        x_diff_sol = -(b1 - b2) / (a1 - a2)

    y1_label = f'$y_1 = {a1} * x + {b1}$'
    y2_label = f'$y_2 = {a2} * x + {b2}$'
    y_diff_label = '$y_{diff} = y_{1} - y_{2}$'

    fig, ax = plt.subplots()
    ax.plot(x, y1, x, y2)
    ax.set(xlabel='x',
           ylabel='y')
    ax.legend([y1_label, y2_label])

    if a1 - a2 != 0:
        ax.plot(x, y_diff, linestyle='--', color='red')
        ax.plot(x_diff_sol, 0, 'o', color='red')
        ax.legend([y1_label, y2_label, y_diff_label])
        title = f"$y_1 - y_2 = 0$ pour $x = {x_diff_sol:.2f}$"
        ax.set_title(title)

    ax.grid()
    plt.show()


x = np.arange(start=-10, stop=10, step=0.1)

a1 = 1 / 2
b1 = 9
param1 = [a1, b1]

a2 = 0
b2 = 1
param2 = [a2, b2]

comparison_1degree(x, param1, param2)

a1 = 1 / 2
b1 = 9
param1 = [a1, b1]

a2 = 1 / 2
b2 = 1
param2 = [a2, b2]

comparison_1degree(x, param1, param2)


a1 = 5
b1 = 45
param1 = [a1, b1]

a2 = 5
b2 = 10
param2 = [a2, b2]

x = np.arange(start=-10, stop=10, step=0.1)
comparison_1degree(x, param1, param2)
