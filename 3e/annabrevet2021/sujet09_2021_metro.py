gcd#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:48:34 2021

@author: cghiaus
"""

import pandas as pd

d = {'Temps': ['2:22', '2:24', '2:26', '2:27', '2:28',
               '2:29', '2:30', '2:31', '2:32', '2:33',
               '2:34', '2:35', '2:38'],
     'Nombre': [1, 1, 2, 6, 3,
                7, 6, 3, 1, 2,
                3, 2, 3]}
df = pd.DataFrame(d)


df['Temps_s'] = pd.to_timedelta("00:" + df['Temps']).dt.total_seconds()

print('No experiments :', df['Nombre'].sum())
