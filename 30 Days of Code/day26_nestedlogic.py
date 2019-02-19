'''
Title     : Nested Logic
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-nested-logic/problem
'''

from datetime import date

# Use map to convert list of str inputs to int
actual = map(int, input().split(' '))
expected = map(int, input().split(' '))

# Cast map object back to list
actual = list(actual)
expected = list(expected)

# Create date objects using the dates passed in
actual = date(day=actual[0], month=actual[1], year=actual[2])
expected = date(day=expected[0], month=expected[1], year=expected[2])


def calc_fine(actual, expected):
    fine = 0

    # Calculating fine only if book returned after expected date
    if actual > expected:
        # If returned within the expected year
        if actual.year == expected.year:
            # And within the expected month
            if actual.month == expected.month:
                # Calculate fine based on num days late
                fine = 15 * (actual.day - expected.day)
            else:
                # Otherwise calculate based on num months late
                fine = 500 * (actual.month - expected.month)
        # If its not within the expected year, it must be over a year late which is a 10k fine
        else:
            fine = 10000

    print(fine)


calc_fine(actual, expected)
