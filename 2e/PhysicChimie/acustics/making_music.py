#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:48:07 2022

@author: cghiaus

https://blog.changshe.io/making-music-in-a-jupyter-notebook-19c57791e636

Making music in a Jupyter notebook
"""

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio


def play(freq, sec=1):
    framerate = 44100   # <- rate of sampling
    t = np.linspace(0, sec, framerate * sec)    # <- setup time values
    data = np.sin(2 * np.pi * freq * t)     # <- sine function formula
    return Audio(data, rate=framerate, autoplay=True)   # play sound


play(440)   # play a sound at 440 hz for 1 second

t = np.linspace(0, 1, 320)
data = np.sin(2 * np.pi * 1 * t)    # <- 1 Hz
plt.plot(t, data)
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
