'''
Title     : More Exceptions
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-more-exceptions/problem
'''
#!/bin/python3


class Calculator:  # No need to extend object class in Py3+
    def power(self, n, p):
        if (n < 0) or (p < 0):
            raise Exception('n and p should be non-negative')
        else:
            return n ** p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
