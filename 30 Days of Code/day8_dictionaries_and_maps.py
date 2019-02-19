'''
Title     : Dictionaries and Maps
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
'''

# Number of test cases
testnum = int(input())
phonebook = {}

# iterating to populate dict with given input
for _ in range(testnum):
    name, number = input().split()
    phonebook[name] = number

for _ in range(testnum):
    name = input()

    if name in phonebook:
        print('{}={}'.format(name, phonebook[name]))
    else:
        print('Not found')
