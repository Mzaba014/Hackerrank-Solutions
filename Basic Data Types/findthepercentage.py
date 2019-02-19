'''
Title     : Finding the percentage
Subdomain : Basic Data Types
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''

if __name__ == '__main__':
    from decimal import Decimal

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_avg = Decimal(sum(student_marks[query_name]) / 3.0)
    student_avg = round(student_avg, 2)

    print(student_avg)
