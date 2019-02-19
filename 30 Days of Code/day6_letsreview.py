'''
Title     : Let's Review
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-review-loop/problem
'''


#!/bin/python

import math
import os
import random
import re
import sys


numcases = int(input())
for _ in range(numcases):
    s = input()
    print('{} {}'.format(s[::2], s[1::2]))
