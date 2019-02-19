'''
Title     : Sorting
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-sorting/problem
'''
#!/bin/python3


def bubblesort(arr, n):
    num_swaps = 0

    # Lead pointer iterates over full length
    for i in range(n):
        # Second pointer iterates to penultimate index
        for j in range(n - 1):
            # If the element to the left is greater than that to the right
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Increase total swaps count
                num_swaps += 1

        # Condition to break out if already sorted
        if not num_swaps:
            break

    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(arr[0]))
    print('Last Element: {}'.format(arr[-1]))


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
bubblesort(arr, n)
