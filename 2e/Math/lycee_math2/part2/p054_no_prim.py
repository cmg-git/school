#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:52:09 2022

@author: cghiaus
"""


# def factors(n):
#     i = 2
#     while True:
#         p = 0     # power
#         while n % i == 0:
#             p = p + 1
#             n = n / i

#         if p != 0:
#             print(i, '^', p)

#         i = i + 1

#         if n == 1:
#             return


def factors(n):
    i = 2
    while n > 1:
        p = 0     # power
        while n % i == 0:
            p = p + 1
            n = n / i

        if p != 0:
            print(i, '^', p)

        i = i + 1


factors(3)
factors(15)
print(factors(25))
print(factors(75))
