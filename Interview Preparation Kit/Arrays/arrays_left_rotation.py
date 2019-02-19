'''
Title     : Arrays: Left Rotation
Subdomain : Interview Preparation Kit
Domain    : Python 3
Author    : Manuel Zabala
Created   : 1/24/2019
Problem   : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the rotLeft function below.


def rotLeft(arr, rotate_num):
    dq = deque(arr)
    # Fastest solution, deques optimized for operations on either end
    dq.rotate(-rotate_num)
    return list(dq)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
