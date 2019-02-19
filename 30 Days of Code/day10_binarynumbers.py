'''
Title     : Binary Numbers
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def bin_counter(num):
    current_count = 0
    max_count = 0

    while num > 0:
        if num % 2 == 1:
            current_count += 1

            if current_count > max_count:
                max_count = current_count

        else:
            current_count = 0

        num //= 2

    return max_count


if __name__ == '__main__':
    n = int(input())
    print(bin_counter(n))
