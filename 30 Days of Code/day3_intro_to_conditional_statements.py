'''
Title     : Intro to Conditional Statements
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-conditional-statements/problem
'''


#!/bin/python3

import sys
import re
import random
import os
import math

"""
If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""


def weirdchecker(n):
    if n % 2 == 0:  # If even
        if n in range(2, 6):
            print('Not Weird')
        elif n in range(6, 21):
            print('Weird')
        elif n > 20:
            print('Not Weird')
    else:  # if odd
        print('Weird')


if __name__ == '__main__':
    N = int(input())
    weirdchecker(N)
