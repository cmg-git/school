#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:27:56 2022

@author: cghiaus

Écrire un programme en Python pour calculer:
    a) 1+2+3+....+101    b) 1+3+5+....+99   c) 151+155+159+...+551
"""
somme = 0
n = 2
for k in range(0, n + 1):
    somme = somme + k
    print("k =", k, "somme =", somme)
print("somme = ", somme, "formule = ", n * (n + 1) / 2)


# 1+2+3+....+101

somme = 0
n = 101
for k in range(n + 1):
    somme += k
    # print(k, somme)
print(somme, n * (n + 1) / 2)

print(sum(range(n + 1)))


# 1 + 3 + 5+....+99

somme = 0
step = 2
n = 99

for k in range(1, n + 1, step):
    somme += k
    print(k, somme)
print(somme)

print(sum(range(1, n + 1, 2)))


# 151+155+159+...+551 = 151 * (1 + 4 + ... + (551-151))

somme = 0
from_to = 151
n = 551
step = 4

for k in range(from_to, n + step, step):
    somme += k
    # print(k, somme_101)
print(somme)

print(sum(range(151, 551 + 4, 4)))
