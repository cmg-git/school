#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:11:59 2023

@author: cghiaus
"""

n = int(input("Entrer un nombre entier positif : "))
S = 0
for i in range(n):
    S = S + i
print("S = ", S)
