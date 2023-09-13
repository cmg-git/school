#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:07:09 2023

@author: cghiaus
"""

x = float(input("Donner un nombre réel : "))
if 3 * x**2 + 5 * x + 1 >= 0:
    print("3x² + 5x + 1 ≥ 0")
else:
    print("3x² + 5x + 1 < 0")
