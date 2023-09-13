#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 13:39:15 2021

@author: cghiaus
"""

# Math 4e Cahier des compétances
#
# # Je caractérise graphiqument la proportionalité
#
# page 58 - 59

# Representer graphiqument les données du tableau :
#
# |Masse de bonbons en *g*| 100 | 200 | 500 |
# |-----------------------|-----|-----|-----|
# |Prix en *€*            |0.80 | 1.6 | 4   |

# In[ ]:
import numpy as np
import matplotlib.pyplot as plt

masse_bonbons = np.array([100, 200, 500])
prix = np.array([0.89, 1.6, 4])

fig1, ax1 = plt.subplots()
ax1.scatter(x=masse_bonbons, y=prix, marker='o', c='r', edgecolor='b')
ax1.plot(masse_bonbons, prix)
ax1.grid(True)
ax1.set_xlabel('Masse bonbons, $g$')
ax1.set_ylabel('Prix, $€$')

x = np.array([2, 3, 5, 6, 7])
y = np.array([3, 4.5, 7.5, 9, 10.5])

print(y / x)
fig1, ax1 = plt.subplots()
ax1.plot(x, y, linestyle='--', marker='o', color='b')
ax1.grid(True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
