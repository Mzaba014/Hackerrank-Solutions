'''
Title     : Lists
Subdomain : Basic Data Types
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/python-lists/problem
'''


if __name__ == '__main__':
    n = int(input())
    list = []

    for _ in range(n):
        raw_command = input().split()

        if raw_command[0] == 'print':
            print(list)

        elif len(raw_command) == 1:
            function = raw_command[0]
            command = 'list.{}()'.format(function)
            eval(command)

        elif len(raw_command) == 2:
            function = raw_command[0]
            arg1 = raw_command[1]
            command = 'list.{}({})'.format(function, arg1)
            eval(command)

        elif len(raw_command) == 3:
            function = raw_command[0]
            arg1 = raw_command[1]
            arg2 = raw_command[2]
            command = 'list.{}({}, {})'.format(function, arg1, arg2)
            eval(command)
