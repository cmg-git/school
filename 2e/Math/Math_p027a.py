#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:38:48 2021

@author: cghiaus
"""

reponse = int(input('Donner un numéro entre 1 et 10 : '))
resultat = 1
for i in range(6):
    resultat = resultat * reponse
print(resultat)
