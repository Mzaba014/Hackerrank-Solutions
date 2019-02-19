'''
Title     : Find a string
Subdomain : Strings
Domain    : Python
Author    : Manuel Zabala
Created   : 1/23/2019
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
'''


import re


def count_substring(string, sub_string):
    # Making use of positive lookahead assertion to find matches without consuming chars. Allows for finding overlapping matches
    pattern = '(?=({}))'.format(sub_string)
    matches = re.findall(pattern, string)
    return len(matches)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
