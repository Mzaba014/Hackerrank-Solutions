'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/write-a-function/problem
'''


def is_leap(year):
    leap = False

    if (year % 4 == 0):
        if(year % 100 != 0 or year % 400 == 0):
            return True

    return leap
