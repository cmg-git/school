#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:19:46 2022

@author: cghiaus
"""

x = float(input("x = "))
expression = 5 * x**2 + 2 * x - 2
if expression > 0:
    print("Expression positive")
elif expression < 0:
    print("Expression négative")
else:
    print("Expression zéro")
