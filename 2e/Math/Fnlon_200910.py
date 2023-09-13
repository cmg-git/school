#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:42:49 2020

@author: cghiaus
"""

for a in range(-10, 11):
    for b in range(-10, 11):
        if (a * b) > (a - b) > (a + b):
            print(a, b)
