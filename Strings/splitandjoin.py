'''
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
'''


def split_and_join(line):
    return('-'.join(line.split()))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
