#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:58:37 2022

@author: cghiaus

Table multiplication
"""
import random

points = 0
for k in range(10):
    n1 = random.randrange(10)
    n2 = random.randrange(10)
    guess = float(input(f'Produit {n1} * {n2} = '))
    if guess == n1 * n2:
        points += 1
    if guess != n1 * n2:
        points += -1

print(f'Ton score est : {points}')
