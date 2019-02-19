'''
Title     : What's Your Name?
Subdomain : Strings
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/whats-your-name/problem
'''


def print_full_name(a, b):
    full_name = 'Hello {} {}! You just delved into python.'.format(a, b)
    print(full_name)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
