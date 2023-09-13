#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:43:56 2022

@author: cghiaus
"""

import numpy as np

n1 = 1
n2 = 1.5
i1 = 60

i2 = np.arcsin(n1 / n2 * np.sin(np.pi / 180 * i1))
i2 = 180 / np.pi * i2
print(f'i2 = {i2:.2f}°')

i3 = i2

i4 = np.arcsin(n2 / n1 * np.sin(np.pi / 180 * i3))
i4 = 180 / np.pi * i4
print(f'i4 = {i4:.2f}°')
