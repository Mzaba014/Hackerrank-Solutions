'''
Title     : String Validators
Subdomain : Strings
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/string-validators/problem
'''


if __name__ == '__main__':
    s = input()
    print(any(element.isalnum() for element in s))
    print(any(element.isalpha() for element in s))
    print(any(element.isdigit() for element in s))
    print(any(element.islower() for element in s))
    print(any(element.isupper() for element in s))
