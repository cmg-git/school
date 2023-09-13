#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:42:49 2020

@author: cghiaus
"""
import matplotlib.pyplot as plt
import numpy as np

for x in np.arange(-1, -0.8, 0.01):
    for y in np.arange(-10, -4, 0.05):
        if (x * y) > (x - y) > (x + y):
            plt.scatter(x, y, marker='.', color='green')
