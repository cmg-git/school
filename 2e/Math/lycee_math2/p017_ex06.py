#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:36:13 2022

@author: cghiaus
"""

import random

nombre_aleatoire = random.randrange(1, 10)
print("Un entier vient d'être tiré au sort entre 1 et 10 inclus")
reponse = 0
nombre_essaie = 0
while reponse != nombre_aleatoire:
    reponse = int(input("Devinez l'entier tiré au sort : "))
    nombre_essaie += 1

print(f"Vous avez trouvé. Nombre d'essais nécessaires {nombre_essaie}")
