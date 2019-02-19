'''
Title     : Find the Runner-Up Score!
Subdomain : Basic Data Types
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted_list = sorted(list(set(arr)), reverse=True)
    print(sorted_list[1])
