#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:46:51 2022

@author: cghiaus

On dispose d'une feuille de papier d'épaisseur 0,1 mm.
Combien de fois doit-on la plier au minimum pour que l'épaisseur dépasse
la hauteur de la tour Eiffel 324 m.
Écrire un programme en Python pour résoudre ce problème.
"""

# import numpy as np

# eiffel_tower = 324
# paper = 0.001

# print(np.log2(eiffel_tower / paper))

eiffel_tower = 324
width = 0.001
k = 0
while width < eiffel_tower:
    width = 2 * width
    k = k + 1
print(k, width)
