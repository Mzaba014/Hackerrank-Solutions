'''
Title     : Print Function
Subdomain : Introduction
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/python-print/problem
'''

if __name__ == '__main__':
    n = int(input())

    for number in range(1, n + 1):
        print(number, end='')
