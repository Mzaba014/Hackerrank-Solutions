'''
Title     : Loops
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-loops/problem
'''


#!/bin/python

import math
import os
import random
import re
import sys


def multiples(n):
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n * i))


if __name__ == '__main__':
    n = int(raw_input())
    multiples(n)
