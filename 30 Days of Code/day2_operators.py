'''
Title     : Operators
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-operators/problem
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    tax = meal_cost * (tax_percent / 100)
    tip = meal_cost * (tip_percent / 100)
    print(round(meal_cost + tax + tip))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
