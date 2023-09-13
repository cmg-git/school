#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 19:54:51 2021

@author: cghiaus
"""

import random
import pandas as pd

victoire_Tom = 0
victoire_Lea = 0
egalite = 0
for n in range(1, 2_000_001):
    Tom = random.randint(1, 6)
    Lea = random.randint(1, 6)
    if Tom > Lea:
        victoire_Tom = victoire_Tom + 1
    elif Lea > Tom:
        victoire_Lea = victoire_Lea + 1
    else:
        egalite = egalite + 1

    p_Tom = victoire_Tom / n
    p_Lea = victoire_Lea / n
    p_egalite = egalite / n

    # print(f'{n} \t {Tom} \t {Lea}', end="")
    # print(f'\t {victoire_Tom} \t {victoire_Lea} \t {egalite}', end="")
    # print(f'\t {p_Tom:.2f} \t {p_Lea:.2f} \t {p_egalite:.2f}')

l = [{'n': n, 'Tom': Tom, 'Lea': Lea,
      'V_Tom': victoire_Tom, 'V_Lea': victoire_Lea, 'Egal': egalite,
      'p_Tom': p_Tom, 'p_Lea': p_Lea, 'p_egal': p_egalite}]
print(pd.DataFrame(l))
