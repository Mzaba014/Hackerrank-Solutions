'''
Title     : Arrays
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-arrays/problem
'''


#!/bin/python3

import math
import os
import random
import re
import sys


def printreversed(arr):
    for num in reversed(arr):
        print(num, end=' ')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    printreversed(arr)
