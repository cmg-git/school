#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:53:30 2023

@author: cghiaus
"""

V = float(input("entrer une valeur supérieure à 5000 : "))
if V <= 5000:
    print("la valeur n'est pas supérieure à 10.")
else:
    n = 0
    while V >= 2000:
        V = 0.8 * V
        n = n + 1
        print(f"n = {n:2d} \t V = {V:.2f}")
    print("Il a fallu", n, "années")
