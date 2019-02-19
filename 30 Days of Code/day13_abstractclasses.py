'''
Title     : Abstract Classes
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-abstract-classes/problem
'''

#!/bin/python3


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))
