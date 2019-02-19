'''
Title     : Nested Lists
Subdomain : Basic Data Types
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/nested-list/problem
'''

if __name__ == '__main__':
    from collections import defaultdict

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])

    data_dict = defaultdict(list)

    for score, name in students:
        data_dict[score].append(name)

    second_lowest_gpa = list(sorted(data_dict.keys()))[1]
    for name in sorted(data_dict[second_lowest_gpa]):
        print(name)
