'''
Title     : Exceptions - String to Integer
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
'''
#!/bin/python3

S = input().strip()

try:
    S = int(S)
    print(S)
except ValueError:
    print('Bad String')
