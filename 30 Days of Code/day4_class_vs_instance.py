'''
Title     : Class vs Instance
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-class-vs-instance/problem
'''


class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            initialAge = 0
        self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age in range(13, 18):
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.age += 1
