#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:00:16 2021

@author: cghiaus
"""

import numpy as np
arr = np.array([75, 50, 100])
arr = np.array([3, 2, 4])
print('Le plus grand diviseur commun :', np.gcd.reduce(arr))

print(arr / np.gcd.reduce(arr))

arr = arr / np.gcd.reduce(arr)

np.gcd.reduce(arr)


arr = np.array([3, 2, 4])
gcd = np.gcd.reduce(arr)
arr1 = arr / float(gcd)
np.gcd.reduce(arr1)


