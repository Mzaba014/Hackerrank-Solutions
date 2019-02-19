'''
Title     : Bitwise AND
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-bitwise-and/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def find_max(n, k):
    max_bitwise = 0

    for i in range(1, n + 1):
        for j in range(1, i):
            curr_bitwise = i & j
            if (curr_bitwise > max_bitwise) and (curr_bitwise < k):
                max_bitwise = curr_bitwise
            if max_bitwise == k - 1:
                break

    print(max_bitwise)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        find_max(n, k)


calc_fine(actual, expected)
