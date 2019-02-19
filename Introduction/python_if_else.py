'''
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
'''

N = int(input())

if (N % 2 != 0):
    print('Weird')

if(N % 2 == 0):
    if(N in range(2, 6)):
        print('Not Weird')

    if (N in range(6, 21)):
        print('Weird')

    if (N > 20):
        print('Not Weird')
