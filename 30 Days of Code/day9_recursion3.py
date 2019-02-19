'''
Title     : Recursion 3
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-recursion/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
