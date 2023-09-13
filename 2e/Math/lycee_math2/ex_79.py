#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:21:51 2022

@author: cghiaus
"""

a = int(input("a = "))
b = int(input("b = "))

for k in range(10):
    print(f"{k}, {a}**{k} = {a**k}")

n = 0
while a**n < b:
    n += 1
print(f"n = {n - 1}; {a}**{n - 1} = {a**(n - 1)} < b")
print(f"n = {n}; {a}**{n} = {a**n} >= b")

# d = (1.5**4 * 0.25 * 8.1**2) / (0.03 * 7.5 * 60)
# print(d)

# d = (15e-1**4 * 25e-2 * 81e-1**2) / (3e-2 * 75e-1 * 6e1)
# print(d)

# d = (3**4 * 5**4 * 1e-1**4 * 5**2 * 1e-2 * 3**4 * 1e-2) / (3e-2 * 75e-1 * 6e1)
# print(d)
