#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:26:32 2022

@author: cghiaus
"""

import numpy as np

acid = np.array([0, 2, 4, 5, 6, 8, 10])
base = np.array([10, 8, 6, 5, 4, 2, 0])

print(0.1 * acid + 1.2 * base)
