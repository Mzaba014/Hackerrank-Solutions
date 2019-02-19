'''
Title     : Tuples
Subdomain : Basic Data Types
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
'''


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    tup = tuple(integer_list)

    print(hash(tup))
