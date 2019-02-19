'''
Title     : Inheritance
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-inheritance/problem
'''

#!/bin/python3

from statistics import mean


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = round(mean(self.scores))

        if avg < 40:
            return 'T'
        elif avg in range(90, 101):
            return 'O'
        elif avg in range(80, 90):
            return 'E'
        elif avg in range(70, 80):
            return 'A'
        elif avg in range(55, 70):
            return 'P'
        elif avg in range(40, 55):
            return 'D'
